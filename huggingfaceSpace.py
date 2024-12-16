import gradio as gr
import joblib
import pandas as pd
import urllib.parse
import re

# Load the trained model
model = joblib.load("randomForestIsItPhishing2.pkl")

# Full feature list (87 features)
FEATURES = [
    "length_url", "length_hostname", "ip", "nb_dots", "nb_hyphens", 
    "nb_at", "nb_qm", "nb_and", "nb_or", "nb_eq", "nb_underscore", 
    "nb_tilde", "nb_percent", "nb_slash", "nb_star", "nb_colon", 
    "nb_comma", "nb_semicolumn", "nb_dollar", "nb_space", "nb_www", 
    "nb_com", "nb_dslash", "http_in_path", "https_token", 
    "ratio_digits_url", "ratio_digits_host", "punycode", "port", 
    "tld_in_path", "tld_in_subdomain", "abnormal_subdomain", 
    "nb_subdomains", "prefix_suffix", "random_domain", 
    "shortening_service", "path_extension", "nb_redirection", 
    "nb_external_redirection", "length_words_raw", "char_repeat", 
    "shortest_words_raw", "shortest_word_host", "shortest_word_path", 
    "longest_words_raw", "longest_word_host", "longest_word_path", 
    "avg_words_raw", "avg_word_host", "avg_word_path", "phish_hints", 
    "domain_in_brand", "brand_in_subdomain", "brand_in_path", 
    "suspecious_tld", "statistical_report", "nb_hyperlinks", 
    "ratio_intHyperlinks", "ratio_extHyperlinks", "ratio_nullHyperlinks", 
    "nb_extCSS", "ratio_intRedirection", "ratio_extRedirection", 
    "ratio_intErrors", "ratio_extErrors", "login_form", 
    "external_favicon", "links_in_tags", "submit_email", 
    "ratio_intMedia", "ratio_extMedia", "sfh", "iframe", 
    "popup_window", "safe_anchor", "onmouseover", "right_clic", 
    "empty_title", "domain_in_title", "domain_with_copyright", 
    "whois_registered_domain", "domain_registration_length", 
    "domain_age", "web_traffic", "dns_record", "google_index", 
    "page_rank"
]

# Feature extraction function
def extract_features_from_url(url):
    """
    Extracts all 87 features from a given URL.
    """
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    
    # Parse URL
    parsed_url = urllib.parse.urlparse(url)
    netloc = parsed_url.netloc
    path = parsed_url.path

    # Calculate features
    features = {
        "length_url": len(url),
        "length_hostname": len(netloc),
        "ip": 1 if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", netloc) else 0,
        "nb_dots": netloc.count('.'),
        "nb_hyphens": netloc.count('-'),
        "nb_at": url.count('@'),
        "nb_qm": url.count('?'),
        "nb_and": url.count('&'),
        "nb_or": url.count('|'),
        "nb_eq": url.count('='),
        "nb_underscore": url.count('_'),
        "nb_tilde": url.count('~'),
        "nb_percent": url.count('%'),
        "nb_slash": url.count('/'),
        "nb_star": url.count('*'),
        "nb_colon": url.count(':'),
        "nb_comma": url.count(','),
        "nb_semicolumn": url.count(';'),
        "nb_dollar": url.count('$'),
        "nb_space": url.count(' '),
        "nb_www": url.lower().count('www'),
        "nb_com": url.lower().count('.com'),
        "nb_dslash": url.count('//'),
        "http_in_path": 1 if "http" in path else 0,
        "https_token": 1 if "https" in netloc else 0,
        "ratio_digits_url": sum(c.isdigit() for c in url) / len(url),
        "ratio_digits_host": sum(c.isdigit() for c in netloc) / (len(netloc) or 1), # Avoid division by zero
        "punycode": 1 if "xn--" in netloc else 0,
        "port": 1 if ":" in netloc else 0,
        "nb_subdomains": netloc.count('.'),
        "prefix_suffix": 1 if "-" in netloc else 0,
        # Other features with default values
    }

    # Fill missing features with 0
    for feature in FEATURES:
        if feature not in features:
            features[feature] = 0
    
    return pd.DataFrame([features], columns=FEATURES)

# Prediction function
def predict_url(url):
    """
    Predicts if a URL is phishing or legitimate.
    """
    # Extract features
    features_df = extract_features_from_url(url)
    
    # Make prediction
    prediction = model.predict(features_df)
    return "Phishing" if prediction[0] == 1 else "Legitimate"

# Gradio Interface
inputs = gr.Textbox(label="Enter URL", placeholder="e.g., google.com")
outputs = gr.Textbox(label="Prediction")

gr.Interface(
    fn=predict_url,
    inputs=inputs,
    outputs=outputs,
    title="Phishing Detection Model",
    description="Enter a URL to predict whether it is Phishing or Legitimate.",
    allow_flagging="manual",  # Default behavior (flagging enabled)
    flagging_dir="flagged_data"  # Directory to save flagged examples
).launch()

