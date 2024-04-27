from nl2ltl import translate
from nl2ltl.engines.gpt.core import GPTEngine, Models
from nl2ltl.filters.simple_filters import BasicFilter
from nl2ltl.engines.utils import pretty

engine = GPTEngine(model=Models.GPT4.value, prompt="cyber/new-prompt.json")
filter = BasicFilter()

utteranceMap = {
    "T1566": "Attackers leveraged spearphishing emails with malicious links to gain access to the system",
    "T1548": "Attackers modifies the tty_tickets line in the sudoers file to gain root access",
    "T1048": "Exfiltration over standard encrypted web protocols to disguise the exchanges as normal network traffic",
}

for i in range(len(utteranceMap)):
    if i == len(utteranceMap)-1:
        break
    utterance = utteranceMap[(list(utteranceMap.keys())[i])] + ". This leads to: " + utteranceMap[(list(utteranceMap.keys())[i+1])]
    print("\n", utterance)
    ltlf_formulas = translate(utterance, engine, filter)
    pretty(ltlf_formulas)