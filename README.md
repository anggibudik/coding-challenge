# Anggi's Coding Challenges Dump

> Still under construction. Also need to move a lot of solutions from other repositories I had in the past :')

Welcome! This is where I put my solutions over any coding practices and challenges I've ever done across the internet.

## Solution Script
I generally provided two solution scripts for each problem (for each language, if any),
- `basic.*` → a basic problem solving techique with MVP quality (MVP = Minimum Viable Product). This won't guarantee to pass even a basic edge case, but enough to give a basic understanding of problem solving in the coding test/challenge world :")
- `advance.*` → a more advance technique where both edge and corner cases are considered. This solution should achieve 100% passing rate over all given test cases, otherwise I won't include the code here.

In some cases, I just provided a `basic.*` script because it is quite easy to solve and/or has a 100% passing rate even with basic logic :)

## Runtime Error Simulation
If we run the script in our local, chances are the script runs "normally" without any runtime error stopping us. But, it may actually consume either a long execution time (time complexity) or large memory resource (auxiliary space complexity). Think of our old lil' buddy big O notation `O(n)`.

To simulate this, I've included (in most of the scripts) a "runtime error simulator" that mimics the common coding test platform's environment who throws runtime error over non-code issues.

By the time you read this, I mimic Hackerrank specifications below:
- Time limit: 10 seconds
- Memory limit: 512 MB
- Script size limit: 50 kB (currently ignored)

If any of those conditions are `True`, the script will tell us that we're actually failed.

## Programming Language

I'm using Python most of the time, so maybe almost all my scripts here are Python-based. Though sometimes I enjoy some other languages such as PHP, JavaScript, and Go; ordered by mastery level :p.

For legacy solutions, I used Python in jupyter notebook :)

## Quiz/Challenge Source

I tried various coding challenge and coding test platforms, so if you're a regular on those sites, chances are you'll immediately recognize the problem or even the code :)