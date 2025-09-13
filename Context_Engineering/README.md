# Context Engineering

**Context Engineering** is a trending system to handle LLMs and Agents and make the interaction with them more efficient and robust to errors.

Below we explain **Context Engineering** components.

## Prompt Engineering

LLMs goal is to generate sequence ```Y``` subject to input sequence ```X``` which could be shown as ```Y|X``` . We can use **Prompt Engineering** to define optimal input sequence ```X``` that will guide the model toward desired ```Y``` .

There are several ways to use **Prompt Engineering** which some are listed below:

* Role Assignment
* Few Shot Examples
* CoT Prompting
* Constraint Setting

## Memory Management

Managing **short term** and **Long term** **memory** will allow the model to remember conversation turns, user information and preferences which will result in robust and personalized answers.

## State Management

To handle complex tasks, **LLM / Agent** must be aware of the current **State**. This will ensure that the model follow every step of the process as it was instructed and also will give it the ability to pause or resume a process.

## RAG

As it was shown in many researches and experiments, the main problem that may result in **hallucination** or **unrelated answers** by LLMs is lack of information about the desired output. **RAG** will **Augment** **Generation** with **Retrieved** information from data sources which will address this problem without the need for additional training steps.

## Tools

Some LLMs are able to use **Tool Calling** or **Function Calling** and perform required task with help of tools. We are able to build custom **Tools** or use available ones to boost **Agents** capabilities in handling problems.