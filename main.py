import mean_var_std
import json

result = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])

# indent=4 giúp thụt lề 4 khoảng trắng cho mỗi dòng
print(json.dumps(result, indent=4))

