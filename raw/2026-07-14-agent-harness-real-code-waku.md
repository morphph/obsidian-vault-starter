# You Can Learn AI Agent Harness In Real Code In 20 Min | Loop Engineering, Memory, Eval, Open Source

**Source:** https://www.youtube.com/watch?v=rvRyBhILrls
**Channel:** Sean's AI Stories (Shen Sean Chan)
**Published:** 2026-07-14 · **Duration:** 20:49 · **Views (at fetch):** 2,520
**Fetch method:** yt-dlp auto-captions (en-orig) → cleaned to plain text
**Note:** 自动字幕，含转录噪声（如 "Asian"→AI agent、"LM"→LLM、"clock code"→Claude Code、"Superbase"→Supabase、"valve"→LLM、人名/repo 名拼写不稳）。原词保留于此，校正见 wiki 精要。

---

## Transcript (auto-caption, verbatim)

Here's a Sean. So, today I'm going to walk you through a real coding example of Asian harness 
system with loop engineering eval and memories. I have open sourced a local first-person assistant 
that will cover the entire four pillars that matters to an Asian system today, which is harness, 
loop, memory, eval and LM ops as we mentioned. Many people were asking me if I could show some real 
examples, so here we are. GitHub is called Waku-Agent under my GitHub called Shen Sean Chan. I'm 
going to walk you through exactly how to use this thing. A working example looks something like 
this. If you have tried Open Claw or Hermes agent, it works very similarly. A very quick example 
would be find me the rest of the World Cup games and add all of them to my calendar. Let's see. So, 
you can see that it checked if you needed some retrieval and then it realized that no retrieval was 
needed. So, now it's running a loop engine here using all the tools such as search the web and it's 
still thinking looping until it's finishing its task. So, you can see that the loop engineering is 
working around the LM agent. And meanwhile, you can click into the tools to see what kind of tools 
are available. And you can click into the loop it to see the live streaming of looping, but we can 
see that in the chat, too. So, we can come back to this overview to watch this system architecture. 
In the meantime, it's showing us how much money it's spending. Currently, we're by default using 
Anthropic APIs, but you can definitely use some cheaper models like open source ones. Cool. I think 
it finished it and then it's asking me if it can access my calendar. I'll just allow it. So, you 
can see this is a completely local agent that ran through the loop to search across the internet 
and eventually create the event on my calendar. So, we can go to my calendar and see, okay, you 
successfully added the Norway game for tonight. I'm a big fan of Holland. Let's see if they could 
win, but I live in London, so I also support England. So, it's going to be a fun game. I think by 
the time when we publish this video, we will already know the result, so we'll see about that. So, 
again, if we recap, we have a history of the entire loop that the agent ran through. Apparently, 
the agent called the create event tool and the search web tool. And you can also check the results 
here where I added the World Cup event between Norway and England for today over here. This is a 
previous event I added for with my friend Sergey. So, if I don't know who Sergey is, I can just ask 
Wakakku and be like, "Who is Sergey?" So, you can see that it did the retrieval. It went through 
the memory system, and then it told me that it went through the gate for retrieval checking, and 
they find out that Sergey is my close friend. We can double check that. So, this kind of 
information usually will be stored in semantic memory because it's durable fact. So, if I click 
into that, I have three main semantic memory here. One is that Sergey is a close friend who loves 
swimming and often cooks delicious food. Raj is a close friend who plays really great tennis and 
always teaches me great British slangs. And for myself, my channel is usually called Shawn's AI 
Stories, and my X account is Shen Shawn Shan. All of my Chinese account is called the Xiao Engine 
Shawn. Okay. I can ask you things like, "What are my social media accounts?" So, again, it 
retrieved the memory again, and it ran through the LLM agent. It turns out that there's no tool 
that's needed, so it just returned the results for me. Okay. What you have seen already is a demo 
of this open-source project that runs through the agent harness with loop, with memory retrieval, 
and last but not least with LLM ops. So, if you click into trace, you can see the exact tracing of 
how much tokens, how much money I have spent, how many LLM calls. And if you scroll down a little 
bit, you can see the exact things that activated the retrieval gate in the system that fetch 
information from the database. And also, what are some of the tasks that took the longest time. So, 
the one that I asked about with the World Cup games took me almost 100 seconds. All of these 
information are actually stored in the local files called traces. I'm going to show you exactly 
where that is in the code, and how we can implement this step by step. Another way to test this is 
using a gateway such as Telegram. So, what you need to do is if you wanted to build a bot yourself, 
you can come to this agent called BotFather. And literally what you do is that you do {slash} 
start, {slash} new bot, and then give it a name. I tried many names, but many of them were taken. 
So, my bot is called Waku Waku AI Bot. So, if I come here and click on start, I can just ask a 
question, be like, "What World Cup game is on my calendar?" Cool, it says that we have the Norway 
game. Just for sure, I can ask, "Who is Raj?" In the meantime, we can see that there should be a 
history. There we go. Yeah, it's real-time over here. Okay, it's been synced here. By the way, 
everything you have seen right now is local. It's stored in your computer, so it's safe and secure 
with your own machine. I can even add a memory to it. I can be like, "Please remember that Vincent 
and I went to Paris to do an entrepreneurship interview together, and now we're both building AI 
startups and doing great." And if we come back here, you can see that it's using the tools. And I'm 
pretty sure it's just users, you see? It says that the user was storing the memory, and it called 
the tool called save note. So, technically now it should have saved the memory. This kind of thing 
should be semantic memory. So, if we click into semantic, you can see that Vincent has a new fact 
called Vincent and the user went to Paris together. Okay. Anyways, what I did was just I just went 
in and showed you how the entire harness and memory and eval and tool calling and loop system 
works, right? For those of you who are not familiar with these kind of things, just remember that 
it's all buzzwords. What I literally demoed just now is exactly what these things mean, okay? And 
now in the in the second part of this video, I will walk through this codebase that I built. And 
ideally, if you're interested, you can click on the star and contribute to this public repo 
together. Are we ready to read the code? Let's get started. Again, we're here on this GitHub repo, 
Shen Shen Chen {slash} Waku {slash} agent. And you can scroll down here to quick start. And 
literally, we just copy this. Okay. Come to a terminal and paste that in. So, you just clone the 
Waku agent. It's trying localhost:778 because 777 was already occupied, but that's fine. So, let's 
come here. So, you can see this is a new repo that we just built, so everything is fresh. All 
right, because we just started a new project, so it's empty. So, in that case, we should go check 
out the project we just run because it should already have something there. Let's come back here. 
And we go to database and click on SQL console and then hit on run. You can see that we've got all 
these data tables right here. I'm also just going to switch back to my previous folder. And if I 
come to dot Waku and check on database, you can see that it's much longer already. All right. And 
this is exactly where we're going to store the data. All right. We have the second thing called 
soul.md. This is basically the system prompt in this open-source project. And you can just modify 
this in the dashboard, too. If you come to memory, and there's a soul file here. And by default 
says, "If you feel Waku Waku, you can often say Waku Waku as part of the catchy phrases." Again, 
feel free to modify and add something like, "Also say muchas gracias when you feel thankful." That 
means thank you very much in Spanish. And you can click on save. And if we come back to the code, 
you will be able to see that it's updated real time. Okay? So, this is your local system prompt, 
soul.md, that will modify your local agent to talk the way you want. We can just test this one more 
time. Maybe click on new chat. I'll just say, "You're the best AI agent in the world." And he says, 
"Muchas gracias." There we go. So, what else is in the code? We have a memory.md, okay? This is 
where we stored some facts or durable facts, okay? These durable facts are the ones that are 
default, and you can see that previously we added Vincent, who I went to Paris together for 
entrepreneurship interview, it's also saved here. If we come back to the chart, that's still the 
semantic memory. If you click into it, right? You can also edit it right here. All right. Now, all 
the stuff that we run are also in the trace here. All right, if we click into that, you can see 
there is a whole list of events that happened. Let's take a few look. Okay, it recorded the tools, 
the tools used, for example, search the web, and then later it shows you the results with uh the 
usage of tokens in and out, and when it happened, all right? And these are very important things 
because if you use some tracing tools like LangFuse or LangGraph, that basically helps you track 
these kind of things. But with a local machine, what you want is to save this in your local 
computer because that's your personal assistant. And of course, if you want to trace this on a 
cloud, you can upgrade this and connect it to Superbase or just use LangFuse directly. Again, this 
project is an implementation of the harness system on your own local machine. What else is here? 
That's pretty much it for the memory stuff. We can also check out the eval folder. Okay. So, there 
are two main folders here. One is called deterministic. Another one is called judge. A 
deterministic place is basically we wrote out some rules of exactly what we want to test, okay? And 
we come back to the system. It's basically here. Right after the agent replied to you, it will go 
through the tracing and then run the eval, okay? Now, we're looking at the deterministic test. When 
we have a few tools, here is checking if Apple Calendar was working perfectly, and this one is 
checking if the working memory is working properly cuz some of cuz sometimes the eval can be very 
simple rules and you can just test if it's working, all right? But sometimes it's not true because 
you might want LLM or AI as a judge. This was also mentioned in our original system design. If you 
zoom in a little bit, after we trace every single run, where we use a valve to to check out some 
very qualitative questions, right? Was this something good or not? Was it healthy or not? So, in 
the code, let's say, we have Anthropic as a judge. It basically runs Anthropic models to assess 
some results, but I didn't write anything complicated here yet. Um for example, this one is for 
testing the response quality. You go crazy, guys. Give a star, clone this repo, and add your own 
test, and you can check it out. All of those will be traced here in the eval, okay? If you click 
into that, it's everything is in the ops tab. What else do we have? So, we also have skills here, 
okay? So, remember we scheduled a meeting for the World Cup. So, we have a skill here that says 
resolve the relative dates, check the memory context for attendees' preferences, call the tool 
create event, uh which will allow the agent to run the tools, okay? So, this is technically a 
memory, too, but it's called procedural memory. It's basically how you expect the agent to act. So, 
if we come back and check out the overview, again, when the user asks a question through the 
gateway, it could be a Telegram, it could be from this chat itself, and then it runs through the 
memory system, it checks if it's going to retrieve memory from these kind of things, and then it's 
going to tell the agent what to do. All we're doing right now is preparing the right context for 
the agent, okay? And the skills is is as I mentioned, the procedural memory, okay? If I click in 
procedural memory, you can see we have two skills here. One is schedule meeting, okay? Which is 
literally what we just saw in the code. We can modify and be like, always add a heart emoji on the 
calendar event, and save that skill. So, the next time if I say, for example, help me schedule a 
meeting with Sam Altman at 10:00 p.m. today in London, and send it. Let's see what's happening. You 
see, it created the event, and then put a heart there. If we check the tools, we can see that uh it 
scheduled this new meeting with Sam Altman. If I check my calendar, you can see right here, meeting 
with Sam Altman with a heart. So, basically the procedure memory worked, which was running the 
updated skill. Guys, this is really fun. We should just keep adding skills to this, okay? You can 
either Well, I I probably need a feature here to let you add it, but you can just add it in the 
code. Remember there's a folder called skills, and currently we have two skills here. You can 
literally just create a new folder here. Let's call it Sean AI story YouTube title. And then within 
this folder, let's create a new file called skill .md. We can just copy this and come here, or you 
can use clock code to write it for you, but we can just do it ourselves. Let's call it Sean AI 
stories YouTube title. And this is just description, let's say uh read Sean's AI stories on YouTube 
and find out the most popular way to write titles given the video content. So, we're just going to 
keep it simple, right? We're going to say read the memory from Sean's YouTube channel and then 
search the web using the tool search web to confirm the latest 5 to 10 videos. And then read the 
user's brief on the latest video content and return a good title like my own style. All right? 
Let's see if it works, okay? Firstly, let's come to the memory and check out the skills, which is 
the procedure memory. You can see that there's a new skill here. If I just create a new chat, so my 
problem is that help me create a new video title for my YouTube channel to promote this Waku agent, 
um which is this current codebase. Let's see. So, let's see the loop. Nice. It searched the web 
first because we asked it to. Still thinking. And then got the results. Cool. It It read my channel 
and then it gave me uh some titles. I I my own AI agent that runs my life. Meet Waku. All right, 
this this skill is not that good, but you see what I mean. You can just make it better by 
continuing to iterate it. And over time, everything will be stored locally. Remember that this 
entire thing is a local host. There's nothing on the cloud. You literally own this agent, just like 
Hermes, just like Openclaw. But it's very simple and straightforward. You literally just clone this 
GitHub repo and then run it and run the dashboard. And then you get it. You have an agent on your 
laptop. Oh, by the way, almost forgot. You need to come to settings and then paste in the API keys 
for the relevant models you have, okay? So, currently I have put in Anthropic key and Gemini key, 
but you can put in other keys, too. Web search, you also need to put in this thing called Tavily 
Tavily API key, okay? Just to keep that in mind, which is something you need to do as a setup. We 
have walked through all the memory stuff and the skills, which is the procedural memory. We also 
walked through the evals. What's left is that in this Waku folder, we have all the code here, okay? 
The gateway literally has the Telegram right here, and we also have a voice mode, which means that 
you can activate it through voice. Uh we can try real quick. We can go for UV run Waku voice. And 
then now it's listening to me, okay? So, it's trying to capture these these activation word. If I 
say, "Waku Waku." Waku Waku. &gt;&gt; Yes, sir. &gt;&gt; So, I'm going to come here. Hey, uh how 
are you two doing today? &gt;&gt; Waku Waku. I'm ready whenever you are. What can I help you with? 
&gt;&gt; I want you to show me what we have set up on our calendar. All right, did the retrieval. 
Running the agent loop. Come on. Good. Look at this. &gt;&gt; Here's what's on your local calendar 
from today onward. Waku Waku. Event when with swim with Sergi sat gel 11 5006 00:00 p.m. Sergi. 
&gt;&gt; My Sergi and Sergi. &gt;&gt; Norway versus England sat gel 11 10:00 00:00 p.m. 12:00 00:00 
a.m. &gt;&gt; Okay, that's it Waku Waku. Thank you very much. So apparently the voice was not that 
good yet. If you guys would love to contribute to this open source, you can work on the voice side. 
I would really appreciate that. And let's build this up together. But you can see that we can use 
voice to control this and how exciting is that? And some of you probably realized that in the 
previous part of this video, you sometimes see Jarvis in this because I previously was calling this 
a Jarvis project. But then I just realized that you know, it's not very exciting. Everybody's 
building a Jarvis. So I just thought about what mean what excitement means, right? And in Japanese 
is Waku Waku. So that's why I wanted Waku Waku to be the wake up word for this voice agent. I'll 
continue to build on this as a fun project. But the point is that you can control this entire 
harness with memory using voice as well. Okay. So that was the gateway and the loop code so here 
can click into agent. You can see that there's this entire loop agent right here. There's an 
iteration. Okay. So by default we set the maximize maximum iterations to be 10. So it's going to 
run through this thing across at least 10 times until it reaches the goal for the LM agent. And the 
model is basically setting up all of these AI models. And memory code right here is basically how 
we store the episodic memory and store or load the procedure memory which are the skills and the 
semantic memory. Okay. Semantic memory. So this is the system. By the way, for the episodic memory 
we haven't covered this so far. Let's come back to the chart. Remember procedure is skill, semantic 
is for the some doable facts which are constantly being updated by this consolidation task. And 
then an episodic one is basically a dated event. For example, I was asking it to to help me label 
all the World Cup games. These are all episodic memory because they're they're dated. On the other 
hand, the semantic memory is basically consolidated every single time when it feels like there's 
some durable facts that it should be saved. And all of these are in these code. You can feel free 
to dive into it and then make it better if you're contributing to this open source. Ops is how 
we're going to run the dashboard, release some new prompts, and how do we do the tracing. Runtime 
is basically it controls all the sessions for every agent run. Tools are very important. Uh we have 
the Apple calendar tool. We can also add in some MCPs, which will be some iterations in the future. 
You can even write some notes, do some search using the Tavily API, okay? These things we have 
already showed you. All the code is right here. And the main app is here. Class Waku, which is 
literally just a Q&amp;A agent because it's thinking about how to respond to you after it has 
digested the model, the client system prompt, messages, tools, maximum iterations, maximum tokens, 
observers, streaming data, all these things. All right, I think this is a very brief walk-through 
of this coding example with an open-source project to go through agent harness as a whole concept. 
Just to recap again, it happens when you have a gateway, when the user is sending a request, and 
all the agents trying to do is how do we prepare the right memory, which could require some task. 
So there there's a retrieval gate here deciding if we should retrieve or not. You know, sometimes 
it skips, sometimes it retrieves. When it retrieves, should it retrieve from procedural memory, 
which is how the agent act, like how do you schedule a meeting, how do you write a title for Sean's 
YouTube channel. Semantic memory, which are some durable facts, right? Who are Sean's friends? 
Who's Sergey? Who's Rach? Who's Vincent, right? And episodic memory, when did Sean exactly build up 
those dates for the World Cup event, for talking to Sam Altman, all these kind of things? Then the 
agent will decide, okay, with all these memories and context, what kind of tools do I want to ask 
and run this entire loop until we're like, okay, we're done. Let's tell the result back and at the 
same time trace all these things that happened with an eval system to test things out, you know, 
release some new prompt when there requires a new update. And at the same time, after the reply, 
the agent will consolidate some of the facts into semantic memory. You see, this is an entire 
walk-through with real code and implementation on the system design that I have shown in the 
previous three videos. I really hope this was very helpful because a lot of people ask me how do we 
actually implement this in code? And if you feel like this video is a bit too complicated for you, 
I highly, highly recommend that you watch some of those previous videos on agent harness, memory 
system, and even Hermes agent. That'll be very helpful for you to understand this video. But for 
those of you who are technical, I hope this was a fun project for you to play around with. Please 
give me a star, come to this GitHub repo waku-agent under Shinkan Chan, write out some pull 
requests, let's contribute to this and make this the best AI personal agent on your local machine. 
And I think this will be fun. If you have any questions, feel free to ask me and leave a comment 
and subscribe and like the video if you liked it. Give me a star on GitHub. I'll see you in the 
next video. Thank you very much.
