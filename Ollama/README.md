# **OLLAMA**
Here i will show you how to use **Ollama** to run LLMs locally on your device.
Keep in mind that if you previously installed **CUDA** and your GPU **Nvidia Drivers**, **Ollama** should be able to use your GPU accelerator and you will have much faster experience using LLMs on your local device.

To download and install **Ollama** you should follow the instructions in [text](https://ollama.com/download/)

You could also pull **Ollama** image using **Docker** by following instructions from [text](https://hub.docker.com/r/ollama/ollama) (recommended)

When **Ollama** is installed, you should download a model.
You have multiple ways to do it:
 1. Using **Ollama** pull method ```ollama pull <model_name>``` (It will take to much time and is not recommended)
 2. Downloading safetensors of a model from [hugging face](https://huggingface.co/).
 3. Downloading GGUF version of a model from [huggin face](https://huggingface.co/).(recommended)

Keep in mind that downloading a model with second and third approach will need extra steps.
For GGUF version you must:
 1. Convert the GGUF to **Ollama** standard format named Modelfile.
 2. introduce it to **Ollama** using ```ollama create my_model```.
 
 You can see an example of a Modelfile in [Modelfile](./ollama_models/gemma-3-4B-it-QAT-Q4/Modelfile)

For Safetensors you must:
 1. Use convert_hf_to_gguf.py from [llama.cpp](https://github.com/ggml-org/llama.cpp) to convert safetensor model to GGUF.
 2. Proceed with GGUF steps.

Now that the model is ready you should be able to use it with ```ollama run my_model```

You can find an example of using local llms with **Ollama** in [ollama.py](./test_chat.py).