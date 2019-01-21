# Treeful Search

> 小樹屋搜尋工具

## 動機

> 官方搜尋並沒有提供排序服務且只能針對日期搜尋

## 目的

> 提供全面性的搜尋功能

## 用法

`people` 用來排序人數
其他有 `price` `name` ...

```python
for treer in sorted_treers(treers, 'people', reverse=False)[:10]:
    if treer.people <= 3:
        print(treer)
        print('---')
```

## 未來

* [ ] 使用 argument parser
* [ ] API 化