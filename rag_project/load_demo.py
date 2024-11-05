import gradio as gr 

def generate_answer(query):
    result=index.query(query,llm=hf)
    target_string ="Helpful Answer:"
    return result[result.find(target_string)+len(target_string):]
    #return result

demo=gr.Interface(fn=generate_answer,
                  inputs=[gr.Textbox()],
                  outputs="text")

demo.launch(debug=True)