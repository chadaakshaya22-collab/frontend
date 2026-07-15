import gradio as gr
import requests

BACKEND_URL ="https://backend-jhaz.onrender.com"


def debug_code(language, code):
    response = requests.post(
        BACKEND_URL,
        json={
            "language": language,
            "code": code
        }
    )

    if response.status_code == 200:
        return response.json()["result"]
    else:
        return f"Error {response.status_code}\n\n{response.text}"


demo = gr.Interface(
    fn=debug_code,
    inputs=[
        gr.Dropdown(
            choices=[
                "Python",
                "Java",
                "C",
                "C++",
                "JavaScript",
                "TypeScript",
                "Go",
                "Rust",
                "PHP",
                "C#",
                "Kotlin",
                "Swift",
                "SQL",
                "HTML",
                "CSS"
            ],
            value="Python",
            label="Select Programming Language"
        ),

        gr.Textbox(
            label="Paste Your Code",
            placeholder="Paste your code here...",
            lines=18
        )
    ],

    outputs=gr.Markdown(label="AI Debugger Result"),

    title=" AI Code Debugger",
    description="Select a language, paste your code, and click Submit."
)

demo.launch()
