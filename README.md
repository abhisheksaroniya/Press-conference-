# Press-conference-
# Project Description 
This project demonstrates how a press conference is conducted between a prominent / notable person of an organisation and multiple jpurnalists or reporters.
# Internal Working 
This project basically employes socket programming with multithreading and mutex.Here, the server is representing the prominent person who has to answer the questions of
multiple journalists.Each  of the journalist is represented as a client ,which establishes a connection with server and once it is established then they can communicate with each other uninterrupted.In real scenario , each journalist has to wait for thir turn to ask , they have to raise their hand and when given a chance , they can ask the questions .To simulate the same ,all the clients can raise their requests(which is equivalent to raise hand in real scenario) at the same time  but only the one who  acquires the lock will be able to communicate while others will be waiting in the order they raised their requests.This is where use of mutex as lock becomes neccessary.
If any clien wants to connect again then it can raise the request again.
# How to run 
1. start the server 
2. run any of the client or multiple clients at the same time and the connection will be established in the same order.
# My Learning from the project 
1. learned socket programming
2. learned multithreading , which helps in parallel excution
3. learned about syncronisation of threads using mutex
# Additional task 
A one to many chat application is developed.
# Link to video Demo
https://drive.google.com/file/d/1-sJUI4p94KxCbUjnHIHmlIh15cqxY-Cr/view?usp=sharing
# References 
1. https://www.thepythoncode.com/article/make-a-chat-room-application-in-python
2.  https://www.geeksforgeeks.org/socket-programming-python/

