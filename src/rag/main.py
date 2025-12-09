from llm_answer import answer_question
print("""\n
┌────────────────────────────────────┐
│      * Welcome to PDF ka Dalal     │
└────────────────────────────────────┘
""".strip())


query = input("PDf ke bare me kya janna chahte ho?\n")

result = answer_question(query)

print(f"\nAnswer:\n{result["answer"]}\n")
