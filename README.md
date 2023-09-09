# **Open LLM Search**

This repository provides code to easily get started with your own fully-fledged inference API for the [Open LLM Search](https://huggingface.co/masonbarnes/open-llm-search) model, based on `llama-2-7b-32k` by Together AI.

# **Setup**
This code requires a capable machine (at least 16GB VRAM) running Hugging Face's open source [text-generation-inference](https://github.com/huggingface/text-generation-inference).

After installing Docker and necessary drivers, you can run the model on text-generation-inference using the following command:
```bash
docker run --gpus all --shm-size 1g -p 8080:80 -v $PWD/data:/data ghcr.io/huggingface/text-generation-inference:1.0.3 --model-id masonbarnes/open-llm-search
```

This will run the model inference API on port 8080. However, the model needs to have webpage content piped in to work properly.

You must copy `.env.example` and rename it to `.env`. Then change the value of `INFERENCE_URL` to the IP address of your inference API including the port (8080). Don't include a trailing slash.

Optionally, you can use set a proxy by setting the `PROXY` value in `.env` to an HTTP proxy URL. This setting may be necessary if Google is blocking your machine from automatic access.

Once done, you can run app.py (not recommended for production), or build the directory as a Docker container and then run it (recommended for production).

Use the API by sending a POST request to the `/generate` endpoint with the `query` JSON parameter set to your query. Happy coding!