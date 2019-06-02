"""
Quiz
-- Slide 7
-- Page 59
"""

from scipy import spatial
import math

v1 = [1, 1, 0, 0, 1]
v2 = [1, 1, 1, 1, 1]
v3 = [0, 1, 1, 1, 0]
v4 = [0, 1, 1, 1, 1]
v5 = [1, 1, 0, 1, 1]


cos_sim = 1 - spatial.distance.cosine(v4, v5)

print(cos_sim)
# print(3./(math.sqrt(3)*math.sqrt(5)))
