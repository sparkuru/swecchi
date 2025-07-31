## 优水寄

1.   `git clone https://github.com/shi9uma/swecchi.git`，`cd swecchi`
2.   `python -m venv swecchi-venv`，`swecchi-venv/Scripts/activate`
3.   `pip install -r 誓约胜利之剑`

## 超线程技术

原理参考莉沫酱的 [超](https://github.com/RimoChan/chao?tab=readme-ov-file#%E5%8E%9F%E7%90%86)，简单来讲就是把 `xx + yy` 符号化成 `fx.__call__(符号x) + fy.__call__(符号y)`，得到以下有向无环图（树）结构：

```bash
fx.__call__(符号x) + fy.__call__(符号y)
├── fx.__call__(符号x)
│   ├── fx
│   └── 符号x
└── fy.__call__(符号y)
    ├── fy
    └── 符号y
```

分析其依赖后确定计算图和执行顺序：例如 `fx.__call__(符号x) + fy.__call__(符号y)` 依赖于 `fx.__call__(符号x)` 和 `fy.__call__(符号y)`，则必须等待二者全部完成，而该二者之间没有依赖关系，可以并行执行（提交给不同的线程，最终将结果整合起来 return）。像这样，以空间换时间实现超线程。使用方法如下：

```python
from utils.聪明幼女 import 超

@超
def test(times):
    res = 0
    for x in range(5):
        res += times ** times
    return res

test(1000)
```

## api 设计

使用 [GraphQL](https://graphql.cn/) 设计 api 交互方式

## 木桶饭

1.   `pip install 'git+https://github.com/facebookresearch/segment-anything.git'`
2.   `pip install roboflow supervision`
3.   `wget -q -O resources/models/sam-vit-h-4b8939.pth 'https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth'`，文件较大，建议用其他软件下载

## references

1.   [恶魔发癫](https://300data.com/item/all_list.html)
2.   [segment-anything](https://blog.roboflow.com/how-to-use-segment-anything-model-sam/)
3.   