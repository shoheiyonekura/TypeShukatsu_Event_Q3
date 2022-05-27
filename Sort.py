def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    flag = False #2重ループ抜けるためのフラグ
    retary = []
    for i in range(len(array)):
        if array[i] >= pivot: #先頭から探してpivot以上を見つけた時
            for j in range(len(array)):
                if i + j == len(array) - 2: #先頭からの探索と末端からの探索がぶつかった場合
                    flag = True #2重ループから抜けるためフラグをTrueに
                    num = i - 1 #グループ分けをするために衝突した点を記録
                    break
                if array[len(array)-1 - j] < pivot: #末端から探索してpivot未満を見つけた場合
                    array[i],array[len(array)-1 - j] = array[len(array)-1 - j],array[i] #見つけた値の交換
                    break
            if flag: #2重ループから抜ける
                break
    #pivotより小さい値のグループと大きい値のグループを再帰的にソート
    #ただ、実行するとlist index out of rangeとなりエラー
    array[:num] = sort(array[:num]) 
    array[num+1:] = sort(array[num+1:])
    
    return array
    
    
    # ここまで記述

if __name__ == '__main__':
    main()