# score_checker
RED = "\033[0;31m"
GREEN = "\033[0;32m"
END = "\033[0m"
score = float(input("Entry score is :"))

if score > 100 or score < 0:
    print(f"{RED}Invalid score ! don't entry -0 and longer then 100{END}")
else:
    if score >= 80 and score <= 100:
        print(f"your score{score},Get {GREEN}A{END}")
    elif score >= 70:  # 70->79
        print(f"your score{score},Get B")
    elif score >= 60:
        print(f"your score{score},Get C")
    elif score >= 50:  # >=50 then 51 52 53 54 55 56 57 58 59
        print(f"your score{score},Get D")
    elif score >= 40:
        print(f"your score{score},Get E")
    else:
        print(f"your score {score} fail F")
# Logic


# print("my score :",score)
