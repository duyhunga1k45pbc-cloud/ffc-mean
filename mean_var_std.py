import numpy as np

def calculate(list):
    # Kiểm tra xem danh sách có đủ 9 phần tử không
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Chuyển list thành mảng Numpy 3x3
    matrix = np.array(list).reshape(3, 3)

    # Tính toán các giá trị
    # axis=0 là theo cột (columns), axis=1 là theo hàng (rows)
    # .tolist() để chuyển từ định dạng mảng Numpy sang list Python thường
    
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), 
            matrix.mean(axis=1).tolist(), 
            matrix.mean().tolist()
        ],
        'variance': [
            matrix.var(axis=0).tolist(), 
            matrix.var(axis=1).tolist(), 
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(), 
            matrix.std(axis=1).tolist(), 
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(), 
            matrix.max(axis=1).tolist(), 
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(), 
            matrix.min(axis=1).tolist(), 
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(), 
            matrix.sum(axis=1).tolist(), 
            matrix.sum().tolist()
        ]
    }

    return calculations