# eincon
Simple translator between einsum subscripts string and ncon subscripts list.

## Examples
```python
import eincon
einstring_list = ["abi,jbc->jaci","jaci,mcbn->jmabin"]
for s in einstring_list:
    ns = ein2ncon(s)
    print("Given einstring  : ",s)
    print("ncon             : ",ns)
    print("back to einstring: ",ncon2ein(ns))
    print("\n")
```
Outputs:
```python
Given einstring  :  abi,jbc->jaci
ncon             :  [[-2, 1, -4], [-1, 1, -3], [-1, -2, -3, -4]]
back to einstring:  bid,aic->abcd


Given einstring  :  jaci,mcbn->jmabin
ncon             :  [[-1, -3, 1, -5], [-2, 1, -4, -6], [-1, -2, -3, -4, -5, -6]]
back to einstring:  acie,bidf->abcdef
```

