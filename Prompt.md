
Write me a single page website using HTML and JavaScript that can benchmark a new API. The new javascript browser API 
works like this, first you check availability with

const canCreate = await ai.canCreateTextSession();

if canCreate is "readily" you must let the user know that the Prompt API is available. If it is anything other 
than readily let the user know if it is "no" or "after-download".

The user can then proceed to press a benchmark button if the prompt API is available. 
To use the Prompt API you invoke it like this

const result = await session.prompt("Write me a poem.");
console.log(result);

where "Write me a poem." is the prompt in this case.

Your task is to exercise this task API and benchmark the time and collect all the responses.
The input prompts are available as a jsonl file input_data.jsonl.
The contents of the file look like

{"key": 1000, "prompt": "Write a 300+ word summary of the wikipedia page \"https://en.wikipedia.org/wiki/Raymond_III,_Count_of_Tripoli\". Do not use any commas and highlight at least 3 sections that has titles in markdown format, for example *highlighted section part 1*, *highlighted section part 2*, *highlighted section part 3*.", "instruction_id_list": ["punctuation:no_comma", "detectable_format:number_highlighted_sections", "length_constraints:number_words"], "kwargs": [{}, {"num_highlights": 3}, {"relation": "at least", "num_words": 300}]}
{"key": 1001, "prompt": "I am planning a trip to Japan, and I would like thee to write an itinerary for my journey in a Shakespearean style. You are not allowed to use any commas in your response.", "instruction_id_list": ["punctuation:no_comma"], "kwargs": [{}]}

Where each line is a new JSON object.

Run the prompt from each JSON object through the session.prompt API. Measure metrics about the characters per second
for the result produced from the session.prompt API. Save the results for each prompt and produce an output file 
output_data.jsonl that can be downloaded.

The format of the output file is as follows

{"prompt": "Write a 300+ word summary ...", "response": "PUT THE session.prompt RESPONSE HERE"}

The site should show progress as each prompt in the input_data.jsonl is evaluated.
Finally show the statistics for characters per second and allow the user to download the result output_data.jsonl.


--- Iteration ---

This is very good can you use a progress bar and show the Characters per second as the test is running