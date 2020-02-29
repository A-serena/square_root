# xの平方根を求める
import sys
while True:
    x = input("正の数値を入力してください ")
    if x == "end":
        sys.exit("終了します")
    try:
        x = float(x)
    except ValueError:
        print(x, "は数値に変換できません")
        continue  # continue は 次へ移る の意味 やり直し ではない！
    except:
        print("予期していないエラーです")
        exit()
    if x <= 0:
        print(x, "は正の値ではありません")
        continue

    print(str(x), "の平方根を今から求めます")
    # x =float(x) #inputで得た値は文字列(str)なので数扱いにさせる

    rnew = x

    while True:
        diff = rnew - x / rnew
        diff = abs(diff)
        while diff > 1.0e-6:  # 差が10^-6より大きければ繰り返す
            r1 = rnew
            r2 = x / r1
            rnew = (r1 + r2) / 2
            diff = r1 - r2
            diff = abs(diff)

        print(str(rnew))
        break
