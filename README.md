## 1. Claude

### I. [Claude](./nbs/01_claude.ipynb)
   0. https://console.anthropic.com/dashboard
   1. Request a response from a conversation with Claude.
   2. Put words in Claude's mouth: combine role assistant and maximum tokens to get simple short answers.
   3. [Add image with questions](https://docs.anthropic.com/en/docs/build-with-claude/vision) - recommend resizing images before uploading
   4. [Add 2 image and find the difference](https://docs.anthropic.com/en/docs/build-with-claude/vision#example-multiple-images)
   5. [Learn cookbook: format output](https://github.com/anthropics/anthropic-cookbook)
   6. Few shot learning: inject few examples into the conversation.
   7. [System prompt: system prompt is a parameter in the request](https://github.com/anthropics/courses/blob/master/prompt_engineering_interactive_tutorial)
   8. Temperature: temperature is a parameter in the request.
   9. Role prompt: assign role in the system prompt.
   10. Prompt template or input template.
   11. XML tags: use specifically XML tags as separators
   12. Long context tips:
   13. Format output
   14. Think step by step
   15. Avoid hallucinations: give Claude an out.
   16. it's best practice to have the question at the bottom after any text or document
   17. [complex prompt from scatch](https://github.com/anthropics/courses/blob/master/prompt_engineering_interactive_tutorial/AmazonBedrock/anthropic/09_Complex_Prompts_from_Scratch.ipynb): 
   18. [search](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/Wikipedia/wikipedia-search-cookbook.ipynb)

### II. [Claude tool user](./nbs/02_claude_tool_user.ipynb)
  1. Four steps to use tool: tools + prompt -> Claude uses a tool -> Extract tool inputs + run code + return output -> Claude uses the output to answer the user.
  2. Force the model to use the tool:
   - Tell model to use the tool in prompt or system prompt.
   - using tool_choice={"type": "tool", "name": "print_sentiment_scores"}
  3. Define task by using using tags and tools.


### III. [LangChain](./nbs/04_lang_chain.ipynb)
  1. ReAct: Synnergizing Reasoning and Acting in Language Models: LLM <---> Tool
      - LLM will decide which tool to use and input parameters for the tool.
      - Run the tool and get the output.
      - Use the output to answer the user.

  2. LangChain Framework: Prompt + Tools + Flow(Graph).
      - Graph: nodes: agent or functions, edges: connect nodes, conditional edges: decisions.
      - Handle multiple threads: using memory + thread_id.
      - Human in the loop: modify state.
      - Anotations: using anotation to define the structure of the data.
  3. 

### IV. [Pydantic](./nbs/08_pydantic.ipynb)
  1. Pydantic: BaseModel is a class that defines the structure of the data.
  2. Optional type: from typing import Optional, List
  3. Constr, conint, ...: set constraints for the data.
  3. Field validator: @field_validator('age')
  4. Field 
  5. model_json_schema
  6. SkipJsonSchema: skip the field in the json schema.
  7. Customize json schema: add more information to the json schema.
  8. PydanticToolsParser: verify output format.
  9. 