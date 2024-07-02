# Explanatory Prompting
GitHub repository for "Mitigating Hallucination within Large Language Models using Explanatory Prompting". Dataset used for experiments taken from ["How Language Model Hallucinations Can Snowball"](https://arxiv.org/abs/2305.13534).

## Python Files
***confidence_estimate.py*** - Program used to generate confidence estimations during the calculations of calibrations when verifying the theoritcal lower bound from [Calibrated Language Models Must Hallucinate](https://arxiv.org/abs/2311.14648).<br>
***run_experiments.py*** - Program used to run trials of experiments on the [Flight Connectivity Dataset](https://github.com/Nanami18/Snowballed_Hallucination) using varying prompting strategies found in the **prompt** directory.<br>

## Experimental Results
**No Prompt** - Baseline experimental trial<br>
**Verified SOTA** - Add "Let's think step by step" prompt to ***run_experiments.py***<br>
**Topological Order** - Add prompt found in **prompts/top_order.txt** to ***run_experiments.py***<br>
**Zero-Shot Explanatory Prompting** - Add prompt found in **prompts/explanatory_prompt.txt** to ***run_experiments.py***<br>
**Few-Shot Explanatory Prompting** - Add prompt found in **prompts/few_shot.txt** to ***run_experiments.py***<br>
