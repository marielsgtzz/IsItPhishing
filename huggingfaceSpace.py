import gradio as gr
import joblib
import pandas as pd

# Loads the trained model
model = joblib.load("randomForestIsItPhishing2.pkl")

FEATURES = [
    "length_url", "length_hostname", "ip", "nb_dots", "nb_hyphens",
    "nb_at", "nb_qm", "nb_and", "nb_or", "nb_eq", "nb_underscore",
    "nb_tilde", "nb_percent", "nb_slash", "nb_star", "nb_colon",
    "nb_comma", "nb_semicolumn", "nb_dollar", "nb_space", "nb_www",
    "nb_com", "nb_dslash", "http_in_path", "https_token", "ratio_digits_url",
    "ratio_digits_host", "punycode", "port", "tld_in_path", "tld_in_subdomain"
]

def predict_phishing(features):
    # Convert input to a DataFrame
    input_data = pd.DataFrame([features], columns=FEATURES)
    prediction = model.predict(input_data)
    return "Phishing" if prediction[0] == 1 else "Legitimate"

# Create Gradio inputs for each feature
inputs = [gr.Number(label=feature) for feature in FEATURES]

# Create the Gradio interface
interface = gr.Interface(
    fn=predict_phishing,
    inputs=inputs,
    outputs=gr.Textbox(label="Prediction"),
    title="Phishing Detection Model",
    description="Enter feature values to predict whether a URL is Phishing or Legitimate."
)

# Launch the interface
interface.launch()
