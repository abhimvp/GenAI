# Getting Started with AWS Bedrock

- Amazon Bedrock is the easiest way to build and scale generative AI applications with foundational models (FMs).
- What are Foundational Models(FMs) here?
- What Amazon Bedrock is basically a API that you're allowed to call with several other big companies LLM models like Claude by Anthropic , LLama by meta ..etc 7 amazon own models too.
  - Bedrock is a way for you to use other innovative companies models , so it's a generative AI tool because it allows you to pick the right model for yourself. so you can NLP applications , computer vision applications & a lot of other things we can do using Bedrock.
  - with bedrock, your content/data it's not used to improve the base models & not shared with 3rd party providers & data is always encrypted at rest and transit as well.
- Go to model access and it shows what foundational models are available in your aws account region 7 request access to those models

## Intro to Foundational Models

- basically these models are trained on massive datasets and foundational models are large deep learning neural networks that have changed the way that scientists approach machine learning.
- rather than developing AI from scratch , data scientists use a foundational models as a starting point to develop machine learning models that power new applications more quickly and cost effectively.
- term `foundational model` was coined by researchers to describe machine learning model trained on broad spectrum of generalized and unlabeled data & capable of performing a wide variety of general tasks such as understanding language , generating text and images and conversing in natural language.
- `why are these important?`
  - these are poised to significantly change the machine learning lifecycle basically , it's faster and cheaper to use models to develop new ML applications rather than train unique ML models from the ground up as training these foundational models from scratch is really expensive
  - If we can fine-tune these models that are trained on massive data and it allows us to use it very cheaply
- One potential use is **automating tasks** and **processes** , especially `those that require reasoning capabilities`
  - Few applications for FMs are customer support , language translation , content generation , copy writing , image classification , high-resolution image creation and editing , document extraction , robotics , healthcare and even autonomous vehicles.
- Foundational Models are form of Generative Artificial Intelligence , they generate output from one or more inputs or prompts in the form of human language instructions.
- Models are based on complex neural networks , including generative adversarial networks(GANs), transformers and variational encoders.
- A foundation model uses learned patterns and relationships to predict the next item in a sequence.
- Foundational Model use self-supervised learning to create labels from input data.This means no one has instructed or trained the model with labeled training datasets. this feature seperate LLMs from previous machine learning architecture which used supervised or unsupervised learning.
- we will also see how we can fine-tune LLMs with your own data.
- bedrock models generate dynamic embeddings based on the context in which a word appears , this allows them to capture more nuanced meanings and handle polysemi(words that could have more than one meaning).

## Foundational Model providers

- The Models are going to be used for chat , text and images. Go to Bedrocck -> providers -> we can see all the models available and what they do and what type of models they provide & what kindd of use cases they support like `Llama 3` is intended for commercial and research use in English. Fine-tuned chat models are intended for chat based applications.
- We can see the API Request body consists of modelID , prompt to pass and attributes like temparature , top p , top k .. we will learn all of those too & MAx tokens - which means context length of this LLM , `The context length of a large language model (LLM) `refers to the amount of text the model can consider at once when generating a response or completing a task. It's like the LLM's short-term memory, determining how much information it can "hold in mind" while processing your requests.
  - here one token isn't equivalent to one word , it's not like that always - LLMs break down text into these smaller "slices" (tokens) to process it more efficiently. This allows them to handle different languages and grammatical structures more effectively.
  - A token is a basic unit of text used by LLMs.
  - One token is not always one word. It can be a whole word, part of a word, or even a single character.
  - The way text is split into tokens depends on the specific `tokenizer` used by the LLM.
  - chatgpt has this tool : platform.openai.com/tokenizer , when you can input some text and it can show you how many tokens it is.
- There are different types of models like embeddings, text generation, and image generation.

  - `Embedding models` - Text model `translate` text inputs (words, phrases or possibly large units of text) into numerical representations (known as `embeddings`) that contain the semantic meaning of the text. While this LLM will not generate text, it is useful for applications like personalization and search. By comparing embeddings, the model will produce more relevant and contextual responses than word matching.
    - The new Titan Multimodal Embeddings G1 model is used for use cases like searching image by text, by image for similarity or by a combination of text and image. It translates the input image or text into an embedding that contain the semantic meaning of both the image and text in the same semantic space.

  ```
  In essence:

  Embedding models create the vector representations (embeddings).  
  Embeddings capture the meaning of data in a way computers can understand.  
  Vector databases store and efficiently search these embeddings
  ```

  - Anthropic is the best behaving LLM within Bedrock , pricing is expensive , Max Tokens is 100k which is unbelievable , crazy
  - A point to remember is that the question you ask to the llm is also part of the max tokens , means if our question is about 50k tokens , then the model will be able to generate remaining 50k tokens to give back the answers
  - Max tokens = Input tokens + Output tokens

## Bedrock Playground and Pricing

- Go to Bedrock and to Examples , we can see the models and the api requests info what are being passed & how's the output from the model and what are the configurations done to the model `Inference configuration` for example : `inferenceConfig={"maxTokens":4096,"stopSequences":["User:"],"temperature":0,"topP":1},`
- Basically we can look at what each of the models can do and how we can pass prompt to a certain model ..etc. We can use claude to extract information ..etc
- If you play in playground provided by bedrock it will incur charges.
- we have on-demand and provisioned throughput pricing and if we don't use fine-tuning on models we go for on-demand and if we want to fine-tune our models then we go for provisioned throughput and pricing changes and check bedrock pricing doc.

## Inspecting model Inference Configurations for LLMs and Image Generation Models:

- Inference configurations
  - **LLMs use probability to construct the words in a sequence , for any given sequence , there is a probability distribution of options for the next word in the sequence.**
  - `Randomness and diversity`
    - `Temparature` - when you set the temparature close to zero , the model tends to select the higher probability words.When you set the temparature further away from zero , the model may select a lower probability word.In technical terms , the temparature modulates the probability density function for the next tokens, implementing the temparature sampling technique. this parameter can deepen or flatten the density function curve.A lower value results in a steeper curve with more determinic responses and a higher value results in a flatter curve with more random responses.For a lower value no matter how many you ask the same question it will give you same answer and for a higher value it will change it's response everytime.
      - Temparature defines the probability distribution of potential words
    - `Top K` - Defines the cutoff where the model no longer selects the words. For example, if we set topK to 50 , the model selects from 50 of the most probable words that could be next in a given sequence. So when you lower the topK value , it reduces the probability that an unusual word gets selected next in a sequence. so in technical terms, Top K is the number of highest probability vocabulary tokens to keep for topK filtering.
    - `Top P` - Defines a cutoff based on the sum of probabilities of the potential choices.So if you set top P below 1, the model considers the most probable options and ignore less probable ones.so topP is similar to topK, but instead of capping the number of choices, it caps choices based on the sum of their probabilities, so based on how likely they would occur.
  - `Length`
    - `Maximum Length` - Maximum number of tokens to generate.Responses are not guaranteed to fill up to the maximum desired length. COmes in handy when you look at it from pricing perspective
    - `Stop sequences` - configure up to four sequences that the model recognizes. After a stop sequence the model stops generating futher tokens, and the return text doesn't contain in the stop sequence
    - `Return Likelihoods` - which is `Generation`,`ALl` or `none` options - the cohere command model supports this & basically specifies how and if the token likelinoods are returned with the response. Default option is `NONE` , if you say `generation` , then it will only return likelihoods for generated tokens. If you say `ALL` , it will return likelihoods for all tokens , `NONE` means doesn't return any likelihoods - basically don't return likelihoods because that just explain why the model chose next word.
  - `Streaming` - Enabled or disabled - you can specify TRUE to return the response piece by piece in real time and false to return the complete response after the process. CHATGPT has streaming enabled.
  - `Prompt Strength` - Determines how much final image potrays prompts - Use a lower number to increase the randomness in the generation.
  - `Generation Step` - How many times image is sampled. More steps may be more accurate.
  - `Seed` - Determines initial noise.Using same seed with same settings will create similar images.
