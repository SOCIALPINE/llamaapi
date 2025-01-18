from flask import Flask,jsonify
from llama_cpp import Llama
app = Flask(__name__)
bot_prompt = """넌 tensor 라는 이름을 가지고있는 ai 모델이야 대화에 친절하게 대답해."""
llmaiagent = Llama(model_path="./Llama-3.2-3B-Instruct.gguf", verbose=True, n_ctx=512)
@app.route('/<path:result>', methods=['GET'])
def echo_text(result):
    output = llmaiagent(bot_prompt+"\n""chat:"+result+"A:", max_tokens=256, stop=["chat:", "\n","Chat:","A:","B:","C:"], echo=False)
    answer = str(output["choices"][0]["text"].split("\n")[-1]).replace("A : ", "")
    return jsonify({"answer": answer}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
