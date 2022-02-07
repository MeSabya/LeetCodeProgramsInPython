# KMP Algorithm (String Matching) Demystified

## Problem statement:
To Find the occurrences of a word W within a main text T.

## Solution 

### Naive Way
>One naive way to solve this problem would be to compare each character of W with T. Every time there is a mismatch, we shift W to the right by 1, then we start comparing again. Let’s do it with an example:

T: DoYouSeeADogHere (it will be a case insensitive search for all examples)
W: dog

![image](https://user-images.githubusercontent.com/33947539/152738120-db99a81a-c660-4d00-93ef-53166b070354.png)

```python
def bruteSearch(W, T):
    # edge case check
    if W == "":
            return -1

    # getting the length of the strings
    wordLen = len(W)
    textLen = len(T)

    # i is the index of text T from where we will start comparing the
    # the word W
    i = 0

    # length of the subtext has to be equal to the length of the word,
    # so no need to check beyond (textLen - wordLen + 1)
    while i < (textLen - wordLen + 1):
        # we set match to false if we find a mismatch
        match = True

        for j in range(wordLen):
            if W[j] != T[i + j]:
                # A mismatch
                match = False
                break

        if match:
            # We found a match at index i
            print "There is a match at " + str(i)

        # incrementing i is like shifting the word by 1
        i += 1

    return -1
```
👉 Time complexity of this naive approach is O(mn), where m and n are length of the word W and the text T respectively.

### Optimized Version 

**T: deadElephant
W: deadEye**

![image](https://user-images.githubusercontent.com/33947539/152739193-11abfac1-330f-4071-9189-e863aefe2180.png)

*Make sure you understand what green cells convey. I will be using a lot of them. In the above image the green cells in the left substring is equal to the green cells in the right substring. It is actually the largest prefix which is also equal to the suffix of the substring till index 4 of the word “deadeye”. Assume for now we have found it somehow, we will work on finding out largest prefix(green cells) later. Now let’s see how it works by taking an abstract example.*

![image](https://user-images.githubusercontent.com/33947539/152739261-5ac0937b-ce86-4670-bee0-4cf05ca03ac1.png)

>str1 = str2 (green cells) and str2 = str3. When there is a mismatch after str2, we can directly shift the word till after str1 as you can see in the image. Green cells actually tell us the index from where it should start comparing next, if there is a mismatch.

I suppose you now understand if we find out green cells for every prefix of the word W, we can skip few unnecessary matches and increase the efficiency of our algorithm. This is actually the idea behind knuth-Morris-Pratt(kmp) algorithm.


### In search of green cells

We will be using aux[] array to store the index. Unlike Naive algorithm, where we shift the word W by one and compare all characters at each shift, we use a value from aux[] to decide the next characters to be matched. No need to match characters that we know will match anyway. Let’s take yet another weird example.

**W: acabacacd**

![image](https://user-images.githubusercontent.com/33947539/152739540-24b38650-daf6-4c70-8eac-13866244d3b0.png)

*m and `i` define the state of our algorithm and signify that prefix of the word W before m is equal to the suffix for the substring till i-1 i.e `W[0…m-1] = W[i-m…i-1]`. For the above image state, 2(value of `m`) is stored in the aux[] array for the substring till index 4(`i-1`).*

```python
def createAux(W):
    # initializing the array aux with 0's
    aux = [0] * len(W)

    # for index 0, it will always be 0
    # so starting from index 1
    i = 1
    # m can also be viewed as index of first mismatch
    m = 0
    while i < len(W):
        # prefix = suffix till m-1
        if W[i] == W[m]:
            m += 1
            aux[i] = m
            i += 1
        # this one is a little tricky,
        # when there is a mismatch,
        # we will check the index of previous
        # possible prefix.
        elif W[i] != W[m] and m != 0:
            # Note that we do not increment i here.
            m = aux[m-1]
        else:
            # m = 0, we move to the next letter,
            # there was no any prefix found which 
            # is equal to the suffix for index i
            aux[i] = 0
            i += 1

    return aux
```
👉 Following will be the aux array for the word acabacacd

![image](https://user-images.githubusercontent.com/33947539/152739656-5618b7c5-ffa9-47c9-9d11-0720d84a11f0.png)


### KMP Algorithm

**T: acfacabacabacacdk
W: acabacacd** 

```python
W = "acabacacd"
T = "acfacabacabacacdk"

# this method is from above code snippet.
aux = creatAux(W)

# counter for word W
i = 0
# counter for text T
j = 0
while j < len(T):
    # We need to handle 2 conditions when there is a mismatch
    if W[i] != T[j]:
        # 1st condition
        if i == 0:
            # starting again from the next character in the text T
            j += 1
        else:
            # aux[i-1] will tell from where to compare next
            # and no need to match for W[0..aux[i-1] - 1],
            # they will match anyway, that’s what kmp is about.
            i = aux[i-1]
    else:
        i += 1
        j += 1
        # we found the pattern
        if i == len(W):
            # printing the index
            print "found pattern at " + str(j - i)
            # if we want to find more patterns, we can 
            # continue as if no match was found at this point.
            i = aux[i-1]
```

![image](https://user-images.githubusercontent.com/33947539/152739852-7278c58d-b66f-4763-bef2-93fe8a05e7e8.png)

### Some important points of observation:

1. When there is a mimatch , previous index tells about where to start comparing next.
2. The above is true for both algorithms, lps construction and KMP algorithm.
            

    




