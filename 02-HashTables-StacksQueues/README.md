# Unit 2: Hash Tables / Stacks / Queues

## TODO

- [x] [PreWork](#PreWork)
- [x] [Session #1](#Session-1)
- [x] [Session #2](#Session-2)
- [ ] HackerRank
- [x] [Additional Exercises](#Additional-Exercises)

## Goals
- Test understanding of run times of each data structure
- Being able to identify the proper data structure to use
- Familiarity with hash tables, heaps, queues, stacks
- Learning how to better communicate in an interview setting
  
## PreWork
### Reading / Review

- <a href="https://guides.codepath.org/compsci/Stacks-and-Queues">Stacks and queues</a>
- <a href="https://guides.codepath.org/compsci/Heaps">Heaps</a>
- <a href="https://guides.codepath.org/compsci/Hash-Tables">Hash tables</a>
- <a href="https://www.youtube.com/playlist?list=PL7zKQzeqjecKERijhtFeWf7OYwt27mfKP">Video- Heaps Interview Question Walkthrough</a>

### Required Challenges
- [x] <a href="https://leetcode.com/problems/isomorphic-strings/description/">Isomorphic strings</a> - Hash table - Easy
- [x] <a href="https://leetcode.com/problems/jewels-and-stones/description/">Jewels and stones</a> - Hash table - Easy
- [x] <a href="https://leetcode.com/problems/happy-number/description/">Happy number</a> - Hash set - Easy
- [x] <a href="https://leetcode.com/problems/top-k-frequent-words/description/">Top K frequent words</a> - Heap - Medium
- [x] <a href="https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/">Find k pairs with smallest sums</a> - Heap - Medium

## Session #1
Communication: https://www.interviewcake.com/coding-interview-tips

### Practice
- [x] [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) - Medium
- [x] [Min Stack](https://leetcode.com/problems/min-stack/) - Easy
- [x] [Implement Queue Using Stack](https://leetcode.com/problems/implement-queue-using-stacks/) - Easy
- [ ] Bonus: [Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/) - Medium
  
### Walkthrough
- https://www.youtube.com/playlist?list=PL7zKQzeqjecKERijhtFeWf7OYwt27mfKP
  
## Session #2
### UMPIRE
|||
|-|-|
| **Understand** | - Choose a “happy path” test case, different than the one provided, and a few edge cases to run through <br />- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem |
| **Match** | - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category |
| **Plan** | - Sketch visualizations and write pseudocode <br />- Walk through a high level implementation with an existing diagram
| **Implement** | - Implement the solution (make sure to know what level of detail the interviewer wants) |
| **Review** | - Re-check that your algorithm solves the problem by running through important examples<br />- Go through it as if you are debugging it, assuming there is a bug
| **Evaluate** | - Finish by giving space and run-time complexity <br/>- Discuss any pros and cons of the solution

### Walkthrough
- UMPIRE: https://hackmd.io/@zXKevDKYS9a3T9goj4clQA/S1CaDzIiV?type=view
- Brick Wall & Find A Celebrity Walkthroughs: https://hackmd.io/onj1sIIsQtONLkZQ1uB8qQ#Week-2---Advanced-Guide
  
### Practice
Practice UMPIRE method & write pseudocode
- [x] [Brick Wall](https://leetcode.com/problems/brick-wall/)
- [ ] Find A Celebrity
  > Suppose you are at a party with n people (labeled from `0` to `n - 1`) and among them, there may exist one celebrity. The definition of a celebrity is that all the other `n - 1` people know him/her but he/she does not know any of them.    
  >
  > **Goal**: You want to find out who the celebrity is or verify that there is not one.
  > **Output**: The number associated with the celebrity, or `-1` if no celebrity present
  >
  >**Constraints**:
  >- The only thing you are allowed to do is to ask questions like: *"Hi, A. Do you know B?"* to get information of whether A knows B. 
  >- You need to find the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).  
  >- You are given a helper function `knows(a, b)-->bool` which tells you whether A knows B. 
  > 
  > Implement a function `findCelebrity(n)-->int`, your function should minimize the number of calls to `knows(a, b)`.
  

## Additional Exercises
- [x] [Implement queue using stacks](https://leetcode.com/problems/implement-queue-using-stacks/description/) - Easy
- [x] [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) - Medium
