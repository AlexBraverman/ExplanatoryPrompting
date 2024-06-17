# Intuitive Prompting
GitHub repository for "Intuitive Prompting". Dataset used for experiments taken from ["How Language Model Hallucinations Can Snowball"](https://arxiv.org/abs/2305.13534).

## Python Files
**confidence_estimate.py** - Program used to generate confidence estimations during the calculations of calibrations when verifying the theoritcal lower bound from [Calibrated Language Models Must Hallucinate](https://arxiv.org/abs/2311.14648).

## Experimental Results
![alt text](https://github.com/AlexBraverman/IntuitivePrompting/blob/main/intuitive_prompting.png?raw=true)

**No Prompt** - Baseline experimental trial<br>
**Verified SOTA** - Add "Let's think step by step" prompt to **insert.py**<br>
**Topological Order** - Add prompt found in **a.txt** to **insert.py**<br>
**Zero-Shot Intuitive Prompting** - Add prompt found in **a.txt** to **insert.py**<br>
**Few-Shot Intuitive Prompting** - Add prompt found in **a.txt** to **insert.py**<br>
