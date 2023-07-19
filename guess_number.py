import random

def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("1から100までの数字を予想してください: "))
        attempts += 1

        if guess < target_number:
            print("もっと大きい数です")
        elif guess > target_number:
            print("もっと小さい数です")
        else:
            print(f"正解です！{attempts}回で当たりました！")
            break

if __name__ == '__main__':
    print("=== 数字を当てるゲーム ===")
    guess_number()
