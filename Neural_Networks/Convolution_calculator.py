"""
Convolution Calculator
"""

W1 = 8
H1 = 8
D1 = 12

# ====================== CONVOLUTION LAYER =========================
conv_input = [W1, H1, D1]
K = 12
F = 3
S = 1
P = 1

W2 = (W1 - F + 2*P) / S + 1
H2 = (H1 - F + 2*P) / S + 1
D2 = K

conv_output = [W2, H2, D2]
#print(conv_output)


# ========================== POOLING ================================
pool_input = [W1, H1, D1]

F = 2
S = 2

W2 = (W1 - F) / S + 1
H2 = (H1 - F) / S + 1
D2 = D1

pool_output = [W2, H2, D2]
#print(pool_output)


# ================== TRANSVERSE CONVOLUTION LAYER ====================
transconv_input = [W1, H1, D1]
K = 1
F = 3
S = 1
P = 1
outP = 0

W2 = (W1 - 1) * S - 2*P + F + outP
H2 = (H1 - 1) * S - 2*P + F + outP
D2 = K

transconv_output = [W2, H2, D2]
print(transconv_output)


# =========================== UNPOOLING =============================
unpool_input = [W1, H1, D1]
F = 2
S = 2
P = 0


W2 = (W1 - 1) * S - 2*P + F
H2 = (H1 - 1) * S - 2*P + F
D2 = D1

unpool_output = [W2, H2, D2]
print(unpool_output)