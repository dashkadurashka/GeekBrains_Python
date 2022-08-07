import json

with open("text7.json", "w", encoding="utf-8") as write_json:
    with open("text_7.txt",encoding="utf-8") as my_f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_f}
        real_profit = [i for i in profit.values() if i > 0]
        result = [profit, {"Общая выручка: ": sum(real_profit) / len(real_profit)}]

        json.dump(result, write_json, ensure_ascii=False, indent=2)




