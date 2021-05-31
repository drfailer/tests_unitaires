-------------------------------------------------------------------------------
-- main.hs
-------------------------------------------------------------------------------

import Exercice

assertFibo :: Int -> Int -> String
assertFibo a b
  | (fibo a) == b = "Test correct for n = " ++ show a
  | otherwise = "fibo n = " ++ show (fibo a) ++ ", expected " ++ show b

main = do
  print $ assertFibo 0 0
  print $ assertFibo 1 1
  print $ assertFibo 2 1
  print $ assertFibo 3 2
  print $ assertFibo 4 3
  print $ assertFibo 5 5
  print $ assertFibo 6 8
  print $ assertFibo 7 13
