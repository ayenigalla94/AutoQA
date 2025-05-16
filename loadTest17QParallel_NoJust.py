import requests
import json
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Azure endpoint & auth
url = "https://parth-m722bnfy-swedencentral.services.ai.azure.com/models/chat/completions?api-version=2024-05-01-preview"
headers = {
    'Content-Type': 'application/json',
    'api-key': '8IXpoVgbHXlSWiDQVN3uji1luZZMp5VuSPbcUPHFcVcsLqIAzUqaJQQJ99BBACfhMk5XJ3w3AAAAACOGlcHJ'
}

def create_payload():
    return json.dumps({
        "messages": [
           {"role": "system", "content": '''Answer questions based on the interaction between a call-center agent and a customer.
Ensure the output follows the JSON format below:
{
    "Question #": "[Question Number]",
    "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
}
Interaction:
Speaker 0:

This call is now being recorded. Okay. So it's nice to meet you, Marissa, and I am taking the place of Ignore anytime he gets back from his vacation. So he already told me that you might be reaching out to me concerning any issue, and I'm glad you did reach out to me. And I'm glad I have this opportunity to resolve the issue as well.

So in this meeting today, we'll be discussing on how to rectify the issue, which is affecting the your campaign presently. Before I proceed, I'd like to confirm just a few things just to be sure I have the right information and I am a direct list. So this is as regards Lee Reed.

Speaker 1:

Yes.

Speaker 0:

Okay. Great. And the x can you could you confirm the x handle

Speaker 1:

for me? At at Lirie Diamonds.

Speaker 0:

Awesome. Awesome. And I am speaking with Marissa? Yes. Oh, great.

And if I can confirm, Marissa Mosse, are you the, would I say, the head of marketing or the one in charge of making any decision concerning running AdZonex?

Speaker 1:

Yes. That is me. Oh,

Speaker 0:

awesome. Awesome. Okay. So yeah. So after confirming that, I'd like to just go through a few things that we are gonna be doing today.

Okay. First of all, we would be discussing as to the issue, what's causing the the location problem. Yet because that's what I see as the issue why you're not spending yet. The campaign is not charging you yet. Okay.

So I looked through your campaign, and I saw that it's saying on the audience estimate that a leak a location is required. So this is as a result of the targeting features, which we are picking where I see you're trying to select a specific radius. Am I correct? That's the ZIP code.

Speaker 1:

Yes.

Speaker 0:

Okay. So if I am correct, you're picking you selected the ZIP code already, and then it brought out this radius.

Speaker 1:

Yeah. Yeah. I I selected the ZIP code, and then I selected a radius within 50 miles of my location.

Speaker 0:

Uh-huh. Okay. So I've been trying to look out for why exactly it's not picking up the location that you choose.

Speaker 1:

Okay.

Speaker 0:

So aside these particular issues, there are just a few more things I wanted to discuss with you concerning the campaign. I wanted to confirm that you you Ichno was unavailable to guide you through this campaign. Right?

Speaker 1:

Yeah. He was unable to guide me through this one. Yeah.

Speaker 0:

Oh, okay. Okay. Okay. Alright. That's fine.

So first of all, I raised the ticket concerning this location that's picking up. Okay. And the team are trying to do a troubleshoot from the back end, but they say there are just a few steps that we must have taken before they can go into any advanced settings just to not, disorganize whatever you must have set for your campaign. So, first things first, we would need to do just a few troubleshooting things. Are you do you have an IT team or someone who handles the domain and all the all of these things?

It's it's myself. Oh, okay.

Speaker 1:

And then if I need any help, like, I can, like, reach out to, like, web our website host or people like that. But most of the time, it's me who implements things.

Speaker 0:

Okay. Awesome. Awesome. So there are a few things we could try. I was thinking of sending these things to you, so you could just take your time indeed in all of these.

But I just wanna go over them first with you before I send them to Okay. So one of the recommended steps was we should probably try to disable browser extensions. If you have any browser extension, could you just disable them for now first?

Speaker 1:

On my browser?

Speaker 0:

Yeah. You know, the extensions, the one that just the little pop ups on the right.

Speaker 1:

Yeah. Perfect. Yeah. Mhmm.

Speaker 0:

So that could be one of the reasons. And have you tried using in your, like, a different computer entirely?

Speaker 1:

I'm sorry. Can you repeat that?

Speaker 0:

Have you tried using a different computer to go into your ads account?

Speaker 1:

I have used my cell phone, but not a different computer.

Speaker 0:

Uh-huh. Okay. Okay. Okay. And on the cell phone, it shows it's the same, basically?

Speaker 1:

Yes.

Speaker 0:

Okay. Because one of the options as well here is we should try using another computer. So you'd have to sign out completely from the ads account on this one and sign in on a separate system, probably laptop or desktop, whichever one you wanna use, and started refresh and click on the location again. So this time, you delete it and then put in the ZIP code again and select the old radio thing and see if it picks up your location.

Speaker 1:

Okay.

Speaker 0:

So it's basically meant to pick up your your location and give you an estimate of audience that the target that your ads will be reaching to. So right now, it is assumed it is not even posting your ads to anyone. That's why you have no charges, no movement, nothing.

Speaker 1:

Yeah. Uh-huh. Okay. So just to test it on this computer right now, I did sign out and then log back in. And then now I'm in the ad center.

Do want me to share my screen?

Speaker 0:

Yeah. That that's fine. I could do that. Okay.

Speaker 1:

Can you see my screen?

Speaker 0:

Uh-huh. Yeah.

Speaker 1:

Okay. So I'm now in the campaign. So we want to go to the location.

Speaker 0:

Next page? Yes. The next page. Yes.

Speaker 1:

Alright.

Speaker 0:

Okay. Scroll down. Down. K. K.

Yep. Right here. Right here. So Mhmm. You'd you'd cancel the one that's populating right now, the 43994.

Just cancel that. Delete it. Uh-huh. Okay. So it's clear.

So

Speaker 1:

And then retyping the

Speaker 0:

ZIP code. Yeah.

Speaker 1:

The ZIP code or the actual address?

Speaker 0:

So you could I would suggest you use your ZIP code. Just use the ZIP code only, and then it will bring up the year.

Speaker 1:

Okay. Okay.

Speaker 0:

Okay. Still the same thing. Could you scroll down a bit? Okay. So could you uncheck these devices?

I mean, it really does not matter. It should still go straight to the

Speaker 1:

Okay.

Speaker 0:

Could we scroll down a bit more? Just a second. Keep going. Okay. Yeah.

Let's go back on. So it's still not picking up the location, basically. So let me see. Maybe we should just try a random ZIP code and see if it's I don't know what it so I want to be able to describe this issue to the back end so we know if it's just yours your account, if it's account specific issue.

Speaker 1:

That makes sense.

Speaker 0:

Actually, this is kinda thing. Still the same thing.

Speaker 1:

Yeah. It

Speaker 0:

could be a bug.

Speaker 1:

Okay.

Speaker 0:

It could be it could be a bug. So and it could be an account specific problem. So let's see. Okay. So I think the best thing is to send you the list of recommended troubleshooting tips.

And if we can try to get this done today Okay. Okay. Let me see. Let me see. So while I'm on the call, I would like us to try a few so I'm sure that, yes, I was there when you did some of these things.

Could you sign up completely again and open do you know how to use the incognito?

Speaker 1:

Yeah.

Speaker 0:

Yeah. So you could just stop sharing, then open a private window and sign in again. Then maybe you can add the screen. You can share the screen at that point. Okay.

You would have to stop sharing. Yeah.

Speaker 1:

Yeah. I'll stop sharing. Yes. Thank you. Okay.

Let's see here. Okay.

Speaker 0:

So just do me a favor. Could you close the other one?

Speaker 1:

Yep. I will close the other one. Yep. Absolutely. Do want me to log out of that one too?

Speaker 0:

Yeah. You need to log out completely and close it, then do everything. I'll press on the. Okay. And you're sure your browser is the latest version?

Speaker 1:

Yes. It should be.

Speaker 0:

Okay. So we need to ensure that as well. And if not, we should try updating if we can.

Speaker 1:

Okay.

Speaker 0:

You're logged out to x. Right?

Speaker 1:

Yeah. Logged out. Signature. Yes. I logged out.

Yep. And then I'm now on the incognito window, and I'm going to ads.

Speaker 0:

Okay. You've have have you logged in to x on the Acognito?

Speaker 1:

Yes.

Speaker 0:

Okay. So yeah. Okay.

Speaker 1:

Do you want me to share my screen again?

Speaker 0:

No. No. No. Just when you signed in, you can share your screen.

Speaker 1:

Okay. Okay. Let me share this. Okay. I'm back here.

Speaker 0:

Awesome. Mhmm. Okay. Let's see. Let's just try again.

K. Okay. Why do I select could you do me a favor? Yeah. Yeah.

Close it. Like, yeah, delete the the ZIP code. Yeah. I need to okay. Click on specific location.

Speaker 1:

Okay.

Speaker 0:

Okay. So let's leave it at this, then sign out again. I'm so sorry. I would I'm stressing you out. The stop sharing and sign back in.

Okay. Yeah. I just wanna be sure we are trying everything possible.

Speaker 1:

Yeah. Absolutely. Okay. Yeah. I'm back in.

Okay. I'm back in. Okay.

Speaker 0:

K. Next. Okay. So okay. So this is what I'm having an issue with.

It comes back automatically. I wanted it I wanted it to be fresh, like, just started it, and then okay, so can can we pause is the is the ads on pause right now?

Speaker 1:

The ads

Speaker 0:

are The campaign. Campaign. Is it paused?

Speaker 1:

It's not paused, so it's trying to run. So it is published.

Speaker 0:

Oh, okay. Okay. So let's pause it for now.

Speaker 1:

Okay. So

Speaker 0:

let's just go back. Yeah.

Speaker 1:

Okay.

Speaker 0:

Okay. First, now edit. All better still. Let's make it look like we're running a new campaign. How about that?

Speaker 1:

Okay. Sorry.

Speaker 0:

Just go to create a new campaign. No. Just leave this and create a new campaign. Yeah.

Speaker 1:

Okay.

Speaker 0:

I just wanna be sure. Okay. So no. No. No.

Before you start yeah. Could you go back? Can I see?

Speaker 1:

Yep.

Speaker 0:

Yes. So down here, could you see where I'm marking on your screen? Okay. Sorry. So okay.

No. No. Just stay. Just stay there. Okay.

So I'll direct you. The objective, the name, the credit card, then down below, you see show advanced settings. Mhmm. Yeah. Click on that.

Speaker 1:

Okay.

Speaker 0:

Switch anyway. Awesome. Okay. So just go enter into the details. Oh, okay.

Yeah. Since we're just testing, let's say we've done everything. So just go down. Yeah. Now you've gone to yeah.

So, yeah, location. So, yeah, click on the radius. Uh-huh. Okay. Now search for the ZIP code.

Fifteen fifteen miles. Okay. Okay. Alright. Just give me a moment.

Let me see if I can try this from my own end Okay. Using my own account.

Speaker 1:

Okay.

Speaker 0:

I'm so sorry for the inconvenience.

Speaker 1:

That's okay.

Speaker 0:

Okay. Let's see. I have done all these. Okay. Could you what's the ZIP code one more time?

Speaker 1:

Just do it again?

Speaker 0:

Yeah. No. No. No. Just tell me your ZIP code.

I'm not sure if using it.

Speaker 1:

836. Mhmm.

Speaker 0:

836?

Speaker 1:

Yeah.

Speaker 0:

Just 836?

Speaker 1:

8 3 6 4 2. 4 2. Mhmm.

Speaker 0:

Okay. Maybe it's Apparently, it's the same thing on my end. Location is required. This is Idaho. Right?

Speaker 1:

What was that?

Speaker 0:

Idaho, the city.

Speaker 1:

Yes. Idaho. Okay.

Speaker 0:

Okay. How about we try this?

Speaker 2:

Mhmm.

Speaker 0:

Could you just cancel all of this, the Meridian? Cancel that, and then click on the specific location.

Speaker 2:

Mhmm.

Speaker 0:

Yeah. Okay. So just use Idaho. So since it's Idaho anyway yeah. The city.

Yeah. The city. You want yeah.

Speaker 1:

And then you want the city?

Speaker 0:

Yeah. Just okay. So let me put it this way. You're looking to you're you're you're selling diamonds. Right?

Mhmm. Jewelries, basically. And Yeah. You just want people whom you can serve easily in your region.

Speaker 1:

Yes. Yep. In my local area. Yeah.

Speaker 0:

In your local area. Yeah. I understand that. And so, usually, we don't advise the radius around the location testing. We don't advise that because the audience might be too minute in the area you wanna serve.

And, I've had a situation. I had a client who was into, computer and technical repair. Basically, he repairs computers and phones. So he wanted to run ads, and we were in a call together. And he said he wanted to use the video's testing as well.

And I told him it would give a very little number of people. And so okay. How do I put this? Technically, I don't know the the, what I say, the least number of audience you can have

Speaker 1:

Okay.

Speaker 0:

For the system not to accept it. So I want to believe there's a particular list number. So I know for sure that on METR, it's 1,000. Once your audience is 1,000, it won't work.

Speaker 1:

Okay.

Speaker 0:

You you might publish, but it won't work. Okay. So on x, he my client had about 3,004 3,000 capacity of the audience because he chose his limited number, and it allowed it. And we moved on, and we published. And this was November 2024.

Speaker 1:

Okay.

Speaker 0:

As of today as of today, he has not been charged once. He was running a rich campaign because he wanted to just gain more followers and just to get his business known in his vicinity in his location. So that was the aim. And then we were on the bridge campaign. And until today, the campaign is still running, but he has not been charged even his time.

And this is because he's been charged per impression. So in x, we charge by when we charge you by per impression, it means there must be up to 8,000 impression on your ads before we can charge whatever amount the system wants to charge you, basically. So it means when I went to check these ads, I saw it has only about 200 impressions, basically. So meaning, it can't it can't be charged yet because it's too little. The impression is getting just too little.

So my point in essence is he has a very small location. I Yeah. He was I think it was a remote area, so not so many people are there. Not so many people interact with x or interact with the social media, basically. So the age group and all of those things limited his ads.

Right. He was fine with it, basically. At least if he's getting 10 people to know about him, he was fine with it. That was his goal. Yeah.

So in this case, this is a sales campaign. Sales campaign tries more when you have a larger audience or you've run ads before such that you have a lot of people who have interacted with your ads and get a retargeting. Mhmm. Right now, I don't know if you've run ads before for Lee Lee Lee diamonds. Have you

Speaker 1:

Yes. On X, we ran a few in November and December.

Speaker 0:

Okay. Awesome. So there's a retargeting.

Speaker 2:

Mhmm.

Speaker 0:

Okay. That's perfect. So I would advise you let the number of of the audience be a little more.

Speaker 1:

Okay.

Speaker 0:

Basically, you would get sales. The only issue I have is I do not understand the nature of your business that well. So I don't know if you've ever offered selling to someone who's a little bit far from you. Mhmm. Do you have a problem with someone a little bit far from you ordering?

Speaker 1:

We do need to be in the local area because we are a brick and mortar store, so we don't sell online.

Speaker 0:

Oh, okay. Okay. So it has to be physical.

Speaker 1:

Yeah. That's why yeah. I was trying to do the radius. But with the other ads that we've done on x Uh-huh. We just use the specific locations, and I just typed in ZIP codes that were around my area rather than use the radius.

Speaker 0:

Oh, okay. Okay. K. Yeah. Okay.

So so I feel like we have two options here. I believe I also believe the radio's thing is not accepting because maybe it's just too small.

Speaker 1:

Okay.

Speaker 0:

Or there is actually a glitch with your accounts. So I would say the easy way out is to use something like either targeting something like this or Brother just to get more followers or get more followers. Basically, to get the audience size to be bigger, basically, so you can run. Either ways, it all boils down to sales. Right?

Speaker 2:

Mhmm.

Speaker 0:

And well well, okay. What I'm just trying to say is we have two options. We either let it go this way, or we could just I would still send you the the recommended troubleshooting tips, and we will try that and probably fix another meeting for after you've tried all of these things. And when we get there or you could just send me an email. If it doesn't work, then I raise another ticket for the team to work further.

So I would have to make them know that, yes, we have done every service you can use. We have tried everything, and I was on the call with you when we tried, and we still did not get any results. So they should be able to work on your accounts from the back end.

Speaker 1:

Yeah.

Speaker 0:

These are fine.

Speaker 1:

Yeah. That would be great. That way Okay. So what we can do is for this current ad that I'm running since I'm on a time schedule for it, I can just change Okay. Use specific locations for it.

Speaker 0:

Then

Speaker 1:

if we could still raise the ticket for my account to see if about the in that way, like, for future campaigns that, like, I'm not committed. Yeah. That would be fantastic.

Speaker 0:

Okay. Awesome. I will do that. I will do that. Perfect.

I think the other thing I wanted to discuss with you is I will be honest with you. I tell most of and all of my clients who are running a sales campaign. The issue is this is a sales campaign, and you're you've opted to be charged for link leak. Am I correct?

Speaker 1:

Yes. Because, well, the reason why I did it, and it might be wrong, but the reason I did it is because, I'm trying to promote an event that's happening in my store. And so I want people to set appointments for that event. So that's why I did the link. Click Oh.

Get them to the appointment page.

Speaker 0:

Okay. Okay. Now I understand that. Mhmm. So it's fine.

I mean, it's totally fine to keep the link with. So this point the only point I have here is what I'm just trying to say is it might be so because from my experience or from best practices

Speaker 1:

Yeah.

Speaker 0:

I do know that when you have a limited audience

Speaker 2:

Mhmm.

Speaker 0:

The algorithm tends to charge you more.

Speaker 1:

Okay.

Speaker 0:

So for instance, let's say you run you run an engagement campaign, for instance, and your audience was, say, 90,000,000 people. Mhmm. And you had a good creative. So there are so many things that is considered for the algorithm. The algorithm considers the recency of your campaign, what you're running it for, is the is whatever the reason is, is it still ahead, or is it past?

If it is ahead, then that means it's recent. Right? So Mhmm. The recency, the relevance of the campaign you're running, your ads, the relevance of the ads to the campaign, and, also, it looks at the quality of the creatives and then the audience that you are serving. So if you're serving solely to an audience and your credit is not so good, the algorithm would charge you a lot more.

So Okay. That's where situations I've seen situations where, clients are charged, up to $4 by impression.

Speaker 1:

Okay.

Speaker 0:

It is on the high price. It is on the high side. And they can't blame, but the reason is because of the audience. It's too small. So even if your credit is not so good, if you tend to raise the audience higher, if you make it there about millions, right Mhmm.

You get to the the algorithm will charge you lesser because it's it's it's it chooses a good time to post your ads. Right? So it's not struggling. It's it's all on auto bid, basically. It's bidding for you to put your ad in a space.

There are other people in your line posting as well at the same time. So it checks the kind of audience, the best time to post, and all of these conditions. So for this situation, our audience is not so much. Mhmm. And it gives me the impression that we will be charged a lot more for the link clicks.

So I saw that the budget was $7 per day. Mhmm. So my best advice is you would be limited a lot because when you have let's say, you have two people who click the link, not necessarily register or do what you actually want them to do. They just click a link, and then you'll be charged for maybe two people clicking or maybe one person, and the and the system probably charges you for $5 for just one person clicking. It means the whole time, the remaining part of a day, you would not get any other person to click because it will stop posting your ads because you don't have enough funds for

Speaker 1:

the Okay. Mhmm.

Speaker 0:

Do you understand? So except you are not setting the daily budget except you are not setting the daily campaign budgets, then I would say, okay. So if you just use up the hundred dollars, but it will show your ads as more as many times in a day as it should show your ads. Right? Yeah.

But if we are setting the cap if we are setting the cap at $7, it's just too small to get actual results, basically. That's just so when we advise our clients or when I advise my own clients, I keep telling them, so there's no if you decide you wanna use $5 for your sales campaign, I can't stop you, but I can't tell you or I I do have to let you know that you probably won't even get a result because your budget as well determines how well the the algorithm will put your ads, basically. So it's it's just like let me use an instance of fire. The more fuel you put in the fire, the brighter it will burn.

Speaker 1:

So Look.

Speaker 0:

Basically. Yes. So it's just an advice.

Speaker 1:

Yeah. That makes sense. Yeah. And I I can do I can remove the daily cap budget and just have a a total spend. Right?

Speaker 0:

Uh-huh. Yeah. You can do that.

Speaker 1:

Then Perfect. That works.

Speaker 0:

Okay. Awesome. Awesome. So, yeah, or like I promised, I will be sending you the email or, say, in less than ten minutes, you'll get the email Okay. For the tips.

And as well, I would raise the ticket immediately so they'll be working on your accounts at the back end. Other than that, we've been able to see we were unable to solve the problem, but we're able to get a temporary solution Yeah. While I work on the permanent solution as well. And Yeah. We've been able to discuss the budgets for the campaign.

Is there any question you would have for me at this time?

Speaker 1:

Should I go back to the other ad and turn it on but to make those changes?

Speaker 0:

Yes, please. Yes, please. Let's just do that right now.

Speaker 1:

Okay. So I'll remove this. I'll even add this to 200. Okay. Okay.

Speaker 0:

Okay. Yeah. Okay. Cool. Okay.

I think we're just running it for the first time. Yeah. So because, usually, when you wanna increase budget, if you were running these ads for, say, if you started running these ads, the learning period is two to four business days, basically, or two to four days. So Yeah. When you leave it for the learning period and then you wanna increase your ads, we usually advise our clients not to do an % increase or 50% increase.

Usually, keep it at between 15 to 20 to 30% increase so that it would not take so much time to learn, and it will not affect your results as well, the performance, basically. So yeah. So since we are just running for the first time, yeah, I wanted to say don't make it a % increase, but since it this is still the first time, then 200 is fine.

Speaker 1:

Perfect. Yeah. Since, technically, it hasn't been showing. Yeah. Perfect.

But it does show that I need to enter a daily budget, though. So do I Yeah.

Speaker 0:

So you could put so I would say it's reasonable to use could we test with 20?

Speaker 1:

So with 20? So I won't be charged extra. Right? Oops. So it's only going to

Speaker 0:

To charge any per day That's 20. Yeah. Okay. So, basically, that's just for, like, ten days. Right?

Speaker 1:

Yeah.

Speaker 0:

That's the duration of the biz the campaign. Ten days. Okay. Well, for now, let's see for now.

Speaker 1:

Okay. And then Can we I know there was an issue with the conversion, so can I just turn the conversion off for now?

Speaker 0:

So what do you wanna track? Say?

Speaker 1:

I just wanna turn the tracking off for now because, like, I know there was an issue where it was saying that we we couldn't it wasn't being tracked.

Speaker 0:

Okay. One moment. Let me just check your I will check

Speaker 1:

Okay.

Speaker 0:

The events manager. Oh, it shows inactive here.

Speaker 1:

Mhmm.

Speaker 0:

Okay. So the back end was unable to effectively use the XPixer?

Speaker 1:

So, yeah, so I went and tried to add the code to my website, but it wanted me to add that code to the website before or after header. And I only have a before header, and I have a before body and an after body, but I don't have an after header. So I don't know if that's what was causing that.

Speaker 0:

K. Were you able to implement the base code, though? The base code, this this part, this first one. Oh, okay. So, like, the base Let's get done with this, and then we'd do that.

Yeah.

Speaker 1:

Perfect. Okay. Wonderful. So I'll just I'll go here. So should I just type in my ZIP codes?

Or and then we can see how Okay.

Speaker 0:

Let's try these first.

Speaker 1:

K.

Speaker 0:

Let's try the ZIP code first.

Speaker 1:

Okay.

Speaker 0:

Perfect. Oh, you're trying different cities just to see? Yeah.

Speaker 1:

These are all cities that are within that 50 mile radius that I was trying to go

Speaker 0:

for. Okay.

Speaker 1:

Yeah. And then okay. Okay. Is that audience too small?

Speaker 0:

No. This is this is good.

Speaker 1:

Okay. Perfect.

Speaker 0:

It's 389,000. Yeah. Not in the millions, but, yeah, this should do.

Speaker 1:

Okay. Perfect. And then so then I just click next and then keep saving it?

Speaker 0:

You know, you could uncheck these devices. I mean, it really doesn't matter.

Speaker 1:

Okay. So it'll show it to

Speaker 0:

all of them. Yeah. It'll show it to all of them.

Speaker 1:

Okay. Perfect.

Speaker 0:

And the optimum the targeting optimum targeting is on REST, optimized targeting? Yeah. Okay. Perfect. So next.

Speaker 1:

And then Mhmm. That's good.

Speaker 0:

The creative. Okay.

Speaker 1:

K. Yeah. Next. Mhmm. Yeah.

Next. Then things. So it's this tracking code. So this base pixel, I put into

Speaker 0:

the code.

Speaker 1:

Mhmm. I I put it in the before body and the and the before header.

Speaker 0:

The before header. You mean on the HTML?

Speaker 1:

Mhmm. Yeah. In the yeah. I pasted it. So because it said it wanted me to paste the code before the closing head tag on all pages, but I don't have specifically, like, a spot where I can put it in the closing head tag.

I only have the before head tag and the before body tag and the after body tag.

Speaker 0:

Oh. Oh, can I see that? Can we just go to the website? Yep.

Speaker 1:

Okay. So Okay. So I have the beforehand tags.

Speaker 0:

Uh-huh.

Speaker 1:

And which is right. This is this the the tracking code that I put it on. Uh-huh. And then the after body tags and then the before body tags. So this is where I'm able to put it in these three Okay.

Yeah.

Speaker 0:

Hold on just a second.

Speaker 1:

Okay. I

Speaker 0:

wanna be sure before Just a moment. Mhmm. Yeah. I'm trying to see if I can bring up someone who specializes in these who has in this. So just to be sure.

Speaker 1:

Yeah. Perfect.

Speaker 2:

Okay.

Speaker 0:

Let me see.

Speaker 1:

Let's see. While we're waiting, I'm gonna turn on let's see. Okay.

Speaker 0:

I'm just trying to verify. And if it's something I might just okay. Yeah. I think I'll just include this. Yeah.

Yeah. Okay. Yeah. I just sent an invite, so I'm waiting.

Speaker 1:

Okay.

Speaker 0:

Hi, Aman. Yes, brother. Yeah. So Marissa?

Speaker 1:

Yes.

Speaker 0:

Okay. So this is Aman. He's a spare he specializes in these xP servers. So, Aman, the issue is okay. Marissa, could you just explain, please?

Speaker 1:

Yes. So when I go to install the base pixel for the tracking code of my campaign, the installation instructions say that we wanna paste the code just before the closing head tag of all pages on our website. So when I go to my website, I can only paste on the before head tags, the after body tags, and the before body tags. I don't have any other option. So I posted it in the before head tags.

This is the conversion tracking code that I copied, but I'm still seeing an error, and it's not tracking because this is the error that I keep seeing. So it doesn't look like it's actually working. And I did also try it in the before body tag code snippet as well, and it didn't work.

Speaker 2:

Okay. Quick question over here. Like, this coding, what do you want to track? Which page?

Speaker 1:

I wanna track so I wanna track a specific page, but, it's my it's a blog page, essentially.

Speaker 2:

But this the website, please?

Speaker 1:

Yeah. You wanna see the code the page that it's gonna be on?

Speaker 2:

Yes, please.

Speaker 1:

Okay.

Speaker 0:

Okay.

Speaker 1:

This is the page.

Speaker 2:

Okay. So now, what I want you to do is that, you know, this page. Okay? Mhmm. So this particular page should be having the code.

Not all the other pages should have the codes. Okay?

Speaker 1:

Okay. So okay. So just that one page?

Speaker 2:

Yes. Just this page should have in the code. Okay? And then you go on the Chrome and put an extension of pixel x pixel. Okay?

So the moment you open this page, it should fire the, you know, conversion you're gonna see on the top right corner if you have an, you know, added extension for that.

Speaker 1:

So first, for this one, so I add so I copied the code. I go back to my website, and I go to that specific page.

Speaker 2:

Yes. And then I everything, first of all. Remove all the, you know, codings which you have added in your website. Just reset everything, and then go particularly with this page only. Alright.

Okay?

Speaker 1:

I'll move that.

Speaker 2:

To mess up again everything.

Speaker 1:

So alright. Okay. So it has been removed. Okay. So I'll just put it on this one specific page.

Speaker 2:

Yes.

Speaker 1:

Okay. Okay. So it's added now.

Speaker 2:

Okay. Now open new tab and put up extension. Yeah. Go on extension page.

Speaker 1:

Mhmm.

Speaker 2:

Chrome extension, and then type XPixel.

Speaker 1:

Here? Type x Yeah.

Speaker 2:

Xpixel. Act six two helper.

Speaker 1:

I'm I'll probably I might have to add it.

Speaker 2:

You have to add that. Yes.

Speaker 0:

Yeah.

Speaker 1:

Okay. So let's see.

Speaker 2:

Okay.

Speaker 1:

Let me get logged in. Okay.

Speaker 2:

Is it done?

Speaker 1:

Yep. I'm sharing my screen now. Okay. So now I'm here. Oops.

I'm at where did it go? Okay. Down.

Speaker 2:

Yes. That's it. So on the top right corner Mhmm. You click on that.

Speaker 1:

Okay.

Speaker 2:

And just pin it. Yeah. There you go. Now now, you know, open your website and go to the blog page. See?

You see over there? There's one one, result on the top right

Speaker 0:

corner. Yeah.

Speaker 1:

I see. Perfect. Okay.

Speaker 2:

Click on that. Click on that. Click on this. K. See, now it's active.

Speaker 1:

Perfect. Okay. Click on, that means it's active. Okay. That makes sense.

Speaker 2:

Alright. That's all from me. Perfect.

Speaker 0:

Yeah. That work? Thank you. Thank you very much, Amlan. Thank you.

Thank you, Amlan. Yeah. Yes.

Speaker 1:

So Perfect. Perfect. Next. And then The events. This one, I need to add to the same

Speaker 0:

To do yeah.

Speaker 1:

K. So to do the same exact thing? So this one is to track a specific event. So

Speaker 0:

Specific. Yes.

Speaker 1:

So if I want them to, like, per se, like okay. So I'm on this page, though. It's tracking, but it's not showing my website any I mean, my blog page anymore.

Speaker 0:

Could you just refresh it? Yeah. I'm gonna come here real quick.

Speaker 1:

Yeah. It's not showing it anymore.

Speaker 0:

Oh, wow. Or I don't think that's an as a result of the extension. Let me let me open your on my own browser.

Speaker 1:

Okay.

Speaker 0:

Yes. I'm supposed to go to

Speaker 1:

So you go to about and then our blog. Moment. And then it's this first one.

Speaker 0:

This first one. Banks. Banks. And

Speaker 1:

Yeah.

Speaker 0:

Yeah. Still not coming up.

Speaker 1:

Okay. So for now, until we can get some more time, just because it's event page, I'm just gonna remove this code, and then we can figure out how to do it. I just don't wanna mess up anything on the

Speaker 0:

And yeah. Okay.

Speaker 1:

Yeah. So now it's back. So the code

Speaker 0:

is blocked. You removed the code. Yeah. It's blocking the okay.

Speaker 1:

Yeah. So that's something maybe we can troubleshoot another time, potentially.

Speaker 0:

Okay. Okay.

Speaker 1:

Yeah. I just the event's next weekend, and so I don't wanna mess up this page.

Speaker 0:

Yeah. I can. Okay.

Speaker 1:

K. Maybe

Speaker 0:

I was thinking maybe we could just set up the meeting tomorrow, and I'll get the the guy on the call, and we'll just see about it again. Or you is this something you want to go to the back end team?

Speaker 1:

Yeah. The back on my the back end team on my side?

Speaker 0:

Yeah.

Speaker 1:

Yeah. I can see. But let's first, let's see. So it says it's running. The ad is live, and we're finding new customers.

So Uh-huh. I how do I remove the the tracking on this so that it doesn't

Speaker 0:

K. Let me see. Could you call me again?

Speaker 1:

Is it like who

Speaker 0:

you are?

Speaker 1:

I just wanna remove the tracking on this ad so that it doesn't show the message, because I don't want it to cause issues since I'm not technically tracking anything.

Speaker 0:

Okay. So go there. Do the conversion events. Uh-huh. The conversion event.

Yep. So, basically, you would definitely need the xPixel Mhmm. To run a sales campaign. It's just it's sort of that's the only way we can track the metrics, the performance of the of the campaign. That's the only way we can know if it's working or not.

So it's something we still need to work on as soon as possible.

Speaker 1:

Okay. So for now so I can't I have to track it?

Speaker 0:

Yeah. We have to get it tracking.

Speaker 1:

So if it's not being tracked right now, does that affect does it mean that my ad's not running?

Speaker 0:

No. No. No. It shouldn't.

Speaker 1:

Okay. Because, like okay. So I I click next. I click next. So it's saved.

Right? So I'm just gonna go through this. But the ad is still showing this, and it's not getting results. So I should have some type of result by the end of tonight. Right?

Speaker 0:

Yeah. Yeah. I just wanna confirm one more time concerning the x ads the pixel. Just a moment.

Speaker 1:

Okay. Perfect. Because the main goal right now is just just to have the campaign run.

Speaker 0:

Yeah. To see some results and, yeah, because the the time cons constitutional. Right?

Speaker 1:

Yeah.

Speaker 0:

Yes. So we can just go ahead. We can go ahead. If you keep running, the campaign would keep running, but we would not just be able to track the performance.

Speaker 1:

Okay. That's fine. So as so this message here is gonna go away as soon as someone clicks my ad and I have some type of results?

Speaker 0:

Yes. Yes. Okay. So I think I wanna try so I'm busy. I want to go to the ad.

Let's see if something comes up. So say I opened the leave branch. So click to RSVP. Right?

Speaker 1:

Yep. Click to RSVP. Yep.

Speaker 0:

Okay. K. So I suppose this works only when I mean, or it should work already because I already clicked the link. Yes. Yeah.

So I'm gonna.

Speaker 1:

Because none of these campaigns that I ran had tracking on it.

Speaker 0:

Oh, okay. Alright. Okay. Does it mean it's still not pending?

Speaker 1:

For what was that?

Speaker 0:

Because I'm still not seeing no. I'm just checking the campaign. I'm checking to see if it's working right

Speaker 1:

now. Perfect.

Speaker 0:

Okay. You know what? Yeah. I think I will just keep monitoring this since it shows running. If by morning, it's still not charging, there's still no charges on it, I will just raise it as an issue as well.

Okay. Yeah. Because it has to there has to be some sort of spend on the account.

Speaker 1:

Yeah. So do we wanna set up a time tomorrow to go to work?

Speaker 0:

Yes. I think let me see. Okay. So we could set up a meeting for tomorrow, say, the afternoon or in this time just to confirm that it's working.

Speaker 1:

Okay. I I will be out away from my computer. I'm working at an event Okay. Tomorrow for, like, most of the day. Do you happen to have any time, like, early like, really early in the morning?

Like, I'm not too sure what your time zone is. But

Speaker 0:

Yeah.

Speaker 1:

I'm in I'm in mountain time. So it was, like, maybe 6AM mountain time or, like, 5PM mountain time.

Speaker 0:

So I'm working out of Canada, Toronto.

Speaker 1:

Okay.

Speaker 0:

Oh, I think oh, okay. So your 7AM is my 9AM. I mean, your 6AM should be my 8AM. Okay. I'm just trying to consider because I would probably not have gotten a response from the team by then.

Speaker 1:

Okay.

Speaker 0:

Yes. So okay. What time is more convenient for me? Let me see what I can do.

Speaker 1:

So early in the morning is good. And then mhmm. So, like, super early in the morning, and then also at, like, 5PM at night is fine. But just for just for a Zoom call. But if we if we can do a phone call, that's fine because I can call if I'm away like, since I'll be away from my computer if we wanna just check-in.

I just I just won't be able to have access to my computer to run

Speaker 0:

it. Computer.

Speaker 1:

But if we were to just to, like, check-in to see, that could work too, and then we can do anytime.

Speaker 0:

Okay. So during the weekend too, you would not be available. Right?

Speaker 1:

I'm available during the weekend. Yeah. I so we can do a call on oh, actually. On when? I'm not I'm not mistaken.

I'm at the account. Okay.

Speaker 0:

Yes. Let's do the phone call. Let's do the phone call. I would be checking from my end. And whatever we need to do, I'll just so if it entails whenever you get home, you just log in to your system, and you I would just give you instructions.

We would figure that out tomorrow on the call.

Speaker 1:

Perfect. That works. Yeah. Because then we we can if we want to yeah. Because I think 5PM mountain time is too late for you.

Because

Speaker 0:

Yeah.

Speaker 1:

Yeah.

Speaker 0:

Yeah.

Speaker 1:

So perfect. But if we can do a phone call just to go over make like, I'm gonna keep an eye on the ads too for today. But if we can go over tomorrow just to make sure it's running, that would be great.

Speaker 0:

Okay. That would be great. That would be great. Let's let's do the call, say, 2PM your time. How does that sound?

Speaker 1:

If you just

Speaker 0:

give me a call. Let me let me just drop my phone number. Do I drop it on the chat here? Or

Speaker 1:

The chat's fine.

Speaker 0:

Okay. On the chat. I'm just still there.

Speaker 1:

Perfect. Let me just find that. Okay.

Speaker 0:

Yep. That's my number.

Speaker 1:

And then is this just a regular number, or do I need to use WhatsApp?

Speaker 0:

No. This is a regular number. You can just call me.

Speaker 1:

Yeah. Perfect. I work with a lot of people in, like, Italy, but you're, like, where

Speaker 0:

you are. Yeah. Oh, okay. Now I understand there.

Speaker 1:

Perfect. Okay. Great. Awesome. So I will keep an eye on this ad, make sure it's up and running.

Hopefully, it is and nothing in Yeah. What the audience, the location that fixed everything, and then we should start doing something in the next couple of hours.

Speaker 0:

Yes. Yes. We should. Yes.

Speaker 1:

We should. Alright. One okay. Awesome. Thank you so much for your help, and then, we'll talk tomorrow.

Speaker 0:

Yes. Looking forward to it, and thank you so much for your time. It was really great.

Speaker 1:

Of course. You too. Thank you.

Speaker 0:

Alright. Do have a good one. Bye bye.

Speaker 1:

Everyone else has left the call.
'''},
            {"role": "user", "content": '''<|eot_id|>
<|start_header_id|>user<|end_header_id|>



    Question 1: Evaluate whether the representative informed the participant that the call is being recorded for quality and training purposes. The disclosure does not need to be verbatim but must clearly communicate that the call is being recorded and offer the participant an opportunity to raise concerns if needed.

Scoring Criteria:
Yes: The representative explicitly mentioned that the call is being recorded for quality or training purposes. The statement should also provide an opportunity for the participant to acknowledge or raise concerns, even if phrased differently.
No: The representative did not mention the recording of the call at any point.
Not Applicable (NA): Select this only if the nature of the call does not require recording disclosure (e.g., internal calls where recording is implicit and pre-approved).

Example Acceptable Responses for ‘Yes’:
"Just a heads-up, this call is being recorded for quality purposes. Let me know if you have any concerns."
"Before we continue, this meeting is recorded for training. Please let me know if that’s an issue."

Example Unacceptable Scenarios for ‘No’:
The representative does not mention recording at any point.
The representative only mentions recording after the participant has already engaged in discussion.
The disclosure is vague or does not indicate that the call is being recorded.
    Answer the following in the format provided:
    {
        "Question #": "1",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 2: Evaluate whether the representative confirmed the X Ads account number or X handle during the call. The confirmation should involve directly verifying the account details with the participant to ensure accuracy. The wording does not need to be exact, but the intent must be clear.

Scoring Criteria:
Yes: The representative explicitly confirmed the X Ads account number or X handle by stating or verifying it with the participant.
No: The representative did not confirm the X Ads account number or handle at any point in the conversation.
Not Applicable (NA): Select this only if the call did not require account confirmation (e.g., general inquiries or calls unrelated to account specifics).
Example Acceptable Responses for ‘Yes’:
"Can you confirm that your X Ads account number is [number]?"
"Just to make sure we're looking at the right account, is your handle [@handle]?"
Example Unacceptable Scenarios for ‘No’:
The representative does not confirm the account number or handle.
The representative assumes the account details without verification.
The representative asks for the account details but does not verify or repeat them for confirmation.
    Answer the following in the format provided:
    {
        "Question #": "2",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 3: Evaluate whether the representative confirmed if the Marketing or Ads Decision Maker was present on the call. The confirmation does not need to follow a strict phrasing but must clearly establish whether the person responsible for marketing/advertising decisions is participating.

Scoring Criteria:
Yes: The representative directly confirmed whether the Marketing/Ads Decision Maker was on the call by asking or verifying their presence.
No: The representative did not confirm the presence of the Marketing/Ads Decision Maker at any point.
Not Applicable (NA): Select this only if determining the presence of a Marketing/Ads Decision Maker was irrelevant to the purpose of the call.
Example Acceptable Responses for ‘Yes’:
"Are we speaking with the person who makes marketing decisions for your team?"
"Just to confirm, is the Marketing Decision Maker on this call?"
"Would you be the right person to discuss marketing strategy, or is someone else involved?"
Example Unacceptable Scenarios for ‘No’:
The representative does not ask or confirm the presence of the Marketing Decision Maker.
The representative assumes the participant's role without verification.
The representative discusses marketing-related topics without confirming decision-making authority.
    Answer the following in the format provided:
    {
        "Question #": "3",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 4: Evaluate whether the representative confirmed if the Budget Decision Maker was present on the call. The confirmation should clearly establish whether the participant has authority over budget-related decisions. The wording does not need to be exact but must convey the intent of verifying decision-making authority.

Scoring Criteria:
Yes: The representative explicitly confirmed whether the Budget Decision Maker was on the call by asking or verifying their presence.
No: The representative did not confirm the presence of the Budget Decision Maker at any point.
Not Applicable (NA): Select this only if confirming the Budget Decision Maker’s presence was not relevant to the call’s purpose.
Example Acceptable Responses for ‘Yes’:
"Are we speaking with the person who oversees budget decisions for your team?"
"Just to confirm, is the Budget Decision Maker on this call?"
"Would you be responsible for budgeting decisions, or is someone else involved?"
Example Unacceptable Scenarios for ‘No’:
The representative does not ask or confirm the presence of the Budget Decision Maker.
The representative assumes the participant has budget authority without verification.
The representative discusses budget-related topics without confirming decision-making authority.
    Answer the following in the format provided:
    {
        "Question #": "4",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 5: Assess whether the representative clearly greeted and introduced themselves to the customer at the beginning of the call. A proper greeting should include both an introduction and an acknowledgment of the customer.

Scoring Criteria:

Good: The representative provides a clear greeting and introduction, including their name and role, and engages with the customer in a friendly manner.
Example Responses:
"Hello, my name is [Name], and I’m a [Role] at [Company]. How are you today?"
"Hi, this is [Name] from [Company]. How’s your day going?"

Average: The representative acknowledges the customer but does not fully introduce themselves or engage in a warm manner.
Example Responses:
"Hello, thank you for joining. Let’s start the meeting."
"Hello, so let’s discuss your business."

Needs Improvement: The representative does not introduce themselves clearly or skips the greeting altogether.
Example Scenarios:
The representative starts the conversation abruptly without acknowledging the customer.
The representative launches into business topics without any greeting.

Not Applicable (N/A): Select this option only if the greeting and introduction were unnecessary for the nature of the call (e.g., a follow-up where rapport was already established).
    Answer the following in the format provided:
    {
        "Question #": "5",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 6: Evaluate whether the representative explicitly mentions or implies how they would add value to the customer or agency in their opening statement. The value statement should indicate how the representative’s product, service, or expertise benefits the customer.

Scoring Criteria:
Good: The representative clearly articulates the value they provide, connecting it to business growth, engagement, reach, sales, or tailored solutions.

Example Responses:
"[Company/Product] helps businesses grow by improving reach, engagement, and sales."
"We provide tailored solutions to help you promote your brand and reach your goals."
Average: The representative mentions assistance or support but does not explicitly connect it to a specific value proposition.

Example Responses:
"I will help you with that."
"[Company/Product] is here to assist you."
Needs Improvement: The representative does not mention any form of value or benefit in their opening statement.

Example Scenarios:
The representative starts the call without any value-oriented statement.
The statement is too generic and does not indicate how the service/product benefits the customer.
Not Applicable (N/A): Select this option only if discussing value was not relevant to the purpose of the call (e.g., a purely technical support or administrative conversation).
    Answer the following in the format provided:
    {
        "Question #": "6",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 7: Good: The representative explicitly states the purpose of the call, outlines key discussion points, and ensures alignment with the customer by securing verbal confirmation.

Example Responses:
"Today, we will walk through understanding your business, your goals, some needs assessment questions, and I can answer a few questions for you."
"This call is to discuss the billing or payment issues you are facing, and then we can discuss optimization."
Average: The representative mentions a general topic or focus for the call but does not clearly outline specific objectives or secure confirmation from the customer.

Example Responses:
"We will look into your Ads account today."
"We will talk about your business."
"We will understand how [Product/Service] works."
Needs Improvement: The representative does not establish a clear agenda or goal for the conversation, leading to potential confusion for the customer.

Example Scenarios:
The call begins without any stated agenda.
The representative dives into discussions without clarifying the purpose of the call.
Not Applicable (N/A): Select this option only if setting an agenda was unnecessary for the nature of the conversation (e.g., a casual follow-up with an existing customer who already understands the purpose).
    Answer the following in the format provided:
    {
        "Question #": "7",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 8: Evaluate whether the representative asked impactful, open-ended questions to understand the customer’s business and goals. The assessment should specifically focus on how the representative discussed the ‘Explanation of Business’—which includes broad discussions around the customer’s company and goal setting.

Scoring Criteria:

Good:
The representative uses open-ended questions that invite the customer to elaborate on their business. These questions help surface useful insights about the customer’s company, challenges, needs, or goals.

Example Responses:

“Could you tell me more about your business?”

“Can you walk me through your current process and any goals you’re working toward?”

Average:
The representative uses closed-ended or limited-scope questions that restrict the customer's responses or fail to spark a broader conversation. These may still relate to the business but do not enable a deep understanding.

Example Responses:

“Is your business on crypto?”

“Do you sell physical products?”

Needs Improvement:
The representative does not ask any questions related to the customer's business, goals, or challenges. This results in a missed opportunity to understand the customer's context.

Example Scenarios:

The topic of the customer's business is never addressed.

Only product features are discussed without attempting to connect them to the customer's business or goals.

Not Applicable (N/A):
Select this option only if understanding the customer’s business was clearly not relevant to the purpose of the call (e.g., password reset, invoice clarification, or shipping inquiry).
    Answer the following in the format provided:
    {
        "Question #": "8",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 9: Evaluate whether the representative asked impactful, open-ended questions to explore the customer’s marketing goals, how they plan to achieve them, and any challenges they face.

Scoring Criteria:

Good:
The representative uses open-ended questions to gain insight into the customer’s marketing goals, challenges, and strategic priorities. These questions should prompt the customer to share meaningful details about their objectives, such as sales targets, online presence, engagement goals, or conversion needs.

Example Responses:

“What are your main marketing goals?”

“What steps are you taking to boost your online presence?”

“What are you looking for from [Company] when you advertise with us?”

“Can you share some of your current marketing priorities or challenges?”

References to specific goals such as: leads, sales, reach, engagement, conversions

Average:
The representative asks closed-ended or surface-level questions that do not fully uncover the customer’s marketing objectives or struggles. These may suggest some awareness of the topic but lack depth or context.

Example Responses:

“What are your marketing goals?” (as a closed-ended question)

“You want to have brand presence.”

Needs Improvement:
The representative does not address marketing goals at all or misses the opportunity to explore how the customer is working toward those goals or what challenges they may face.

Example Scenarios:

No discussion of marketing objectives.

No follow-up or probing when the customer hints at a business goal.

Not Applicable (N/A):
Select this only if marketing goals are clearly irrelevant to the nature of the call (e.g., tech troubleshooting or invoice clarification without a business context).+G10
    Answer the following in the format provided:
    {
        "Question #": "9",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 10: Evaluate whether the representative asked open-ended, insightful questions to explore the customer’s current marketing mix and any existing advertising spend.

Scoring Criteria:

Good:
The representative uses open-ended questions that prompt the customer to share information about other platforms they use for advertising and their experience or performance on those platforms. The goal is to understand the customer’s current marketing approach and allocation of budget.

Example Responses:

“Which other platform do you advertise on, and how has your experience been?”

“What have your results been with Meta or TikTok?”

References to platforms such as: Instagram, Meta, TikTok, Google

Probing questions about performance, results, or spend on those platforms

Average:
The representative asks closed-ended or list-based questions that limit the customer’s response and don’t offer deeper insight into performance or strategy.

Example Responses:

“Do you advertise on Instagram, Meta, TikTok?” (closed-ended question)

Questions that imply a yes/no response without follow-up or probing

Needs Improvement:
The representative fails to explore where the customer is currently advertising or how their marketing spend is distributed, missing a key opportunity to align solutions with the customer’s strategy.

Example Scenarios:

No mention of other marketing channels

No probing into how the customer allocates marketing spend or what results they’ve seen

Not Applicable (N/A):
Select this only if a discussion around marketing channels or spend was clearly irrelevant to the nature of the call (e.g., technical support or internal account issue with no marketing component).
    Answer the following in the format provided:
    {
        "Question #": "10",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 11: Evaluate whether the representative asked effective, open-ended questions to confirm the customer’s target audience and demographic. This assessment helps determine if the representative clearly identified who the customer is trying to reach.

Scoring Criteria:

Good:
The representative uses open-ended questions to encourage detailed responses about the customer’s target audience. These should explore various demographic factors such as age, gender, interests, location, and platform preferences (iOS/Android).

Example Responses:

“What would your target audience and demographic be?”

“Can you describe the age range and specific interests of your ideal customer?”

“Are there particular regions or platforms you’re focused on, like iOS or Android?”

Discussion includes: age range, specific genders, interests, region/location, platform preferences

Average:
The representative uses closed-ended or assumptive questions that restrict the customer’s response or leave out key demographic details.

Example Responses:

“You are targeting women?” (closed-ended question)

“Your target audience is young adults?”

Needs Improvement:
The representative does not ask any questions related to the target audience or demographics, missing a critical component of strategic alignment.

Example Scenarios:

No demographic questions asked

The topic is skipped entirely, even when relevant to the conversation

Not Applicable (N/A):
Select this only if identifying a target audience was clearly not necessary for the nature of the call (e.g., tech troubleshooting or account management unrelated to marketing strategy).
    Answer the following in the format provided:
    {
        "Question #": "11",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 12: Evaluate whether the representative asked effective, open-ended questions to understand the customer's target geography or location. This evaluation focuses on identifying the regions or areas the customer is targeting for their marketing efforts.

Scoring Criteria:

Good:
The representative uses open-ended questions that prompt the customer to provide specific details about the targeted geography or location. These questions should uncover information about cities, states, pin codes, or specific regions where the customer intends to focus their marketing efforts.

Example Responses:

“What region or location are we targeting for this campaign?”

“Which cities or states are you focusing on?”

“Can you tell me about the regions or areas that matter most for your marketing strategy?”

Discussion should include: specific cities, states, pin codes, or geographic regions

Average:
The representative asks closed-ended or vague questions that do not explore the full scope of the customer’s geographic target or fail to prompt a deeper discussion on the customer’s regional focus.

Example Responses:

“What location are you?” (closed-ended question)

“You are situated in New York?”

“You want to target the Midwest?”

Needs Improvement:
The representative does not ask any questions related to geography or location, missing a critical aspect of understanding the customer’s marketing strategy.

Example Scenarios:

No discussion of geographic focus during the call.

The representative skips this aspect even when it's clearly relevant to the customer’s marketing strategy.

Not Applicable (N/A):
Select this only if location or geography was clearly not relevant to the nature of the call (e.g., non-regional or global marketing strategy without location-based targeting).
    Answer the following in the format provided:
    {
        "Question #": "12",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 13: Evaluate whether the representative asked impactful, open-ended questions to discuss the customer’s specific KPIs and metrics for achieving their marketing goals. This includes metrics such as cost per site visit, conversion rates, or return on ad spend.

Scoring Criteria:

Good:
The representative asks open-ended questions that prompt the customer to discuss specific KPIs or metrics related to their marketing campaigns. These questions should encourage the customer to provide detailed insights about how they measure success in their marketing efforts.

Example Responses:

“Do you have any specific KPIs or numbers for this campaign?”

“What are the conversion rates or cost per acquisition you’re aiming for?”

“Can you share the click-through rate (CTR) or return on ad spend (ROAS) that you’re targeting?”

“What metrics do you track to evaluate your campaigns? For example, cost per click (CPC) or cost per install (CPI)?”

References to specific KPIs such as CPSV, CPI, CTR, CPA, ROAS

Average:
The representative asks closed-ended questions that only provide limited insights into the customer’s marketing metrics or do not encourage a deeper conversation about the customer’s KPIs.

Example Responses:

“Are you looking for sales?”

“You want impressions?”

Needs Improvement:
The representative does not ask any questions about specific KPIs or metrics, missing an opportunity to understand the customer’s measurement of success.

Example Scenarios:

No mention of KPIs or metrics during the conversation.

The representative doesn’t explore the customer’s goals in terms of measurable outcomes.

Not Applicable (N/A):
Select this only if discussing KPIs or metrics was clearly not relevant to the purpose of the call (e.g., administrative or support-focused conversation).
    Answer the following in the format provided:
    {
        "Question #": "13",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 14: Evaluate whether the representative asked insightful, open-ended questions to discuss the customer’s conversion tracking mechanism. This includes inquiries about the tools, pixels, or APIs the customer uses to track conversions, such as conversion APIs (CAPI), mobile measurement partners (MMP), or event codes.

Scoring Criteria:

Good:
The representative uses open-ended questions that help the customer elaborate on their conversion tracking mechanisms, including pixels, APIs, or other tools. These questions should delve into how the customer tracks conversions and the systems they use to measure success.

Example Responses:

“Are you using any specific pixels to track conversions?”

“Can you tell me about the conversion APIs (CAPI) you’re using?”

“Do you work with Mobile Measurement Partners (MMP) for tracking purposes?”

“How are you tracking events or conversions on your platform? Do you use an event code?”

References to X pixels, CAPI, MMP, base code, or event codes

Average:
The representative asks closed-ended or shallow questions that don’t encourage the customer to provide detailed information about their tracking setup. These questions may indicate basic knowledge but fail to explore the customer’s unique conversion tracking strategy.

Example Responses:

“You can track conversions from your end?”

“We have X pixel to track.”

Needs Improvement:
The representative does not ask any questions about the customer’s conversion tracking mechanism, missing an opportunity to understand how the customer measures their campaign success.

Example Scenarios:

No mention of conversion tracking tools or processes.

The conversation does not explore the customer’s tracking capabilities.

Not Applicable (N/A):
Select this only if conversion tracking was clearly irrelevant to the purpose of the call (e.g., administrative tasks, tech support, or unrelated inquiries).
    Answer the following in the format provided:
    {
        "Question #": "14",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 15: Evaluate whether the representative asked open-ended questions to explore the customer’s key dates, upcoming events, projects, or seasonal considerations for marketing. This helps understand if the customer has specific timing or seasonal needs for their marketing campaigns.

Scoring Criteria:

Good:
The representative uses open-ended questions that encourage the customer to discuss key dates, upcoming events, or projects. These questions should invite the customer to share information about specific seasons, holidays, or other important dates they want to target with their marketing.

Example Responses:

“Do you have any key dates you would like to advertise for?”

“Is there a specific season or seasonal event you want to focus on?”

“Do you have any upcoming projects or events that would influence your marketing?”

Discussion may include: Christmas, holidays, award season, special events, games, new product launches, etc.

Average:
The representative asks closed-ended or vague questions that limit the customer’s response or don’t prompt detailed insights into key dates or events.

Example Responses:

“You want to advertise in December?”

“Do you want to advertise after spring?”

Needs Improvement:
The representative does not ask about key dates, events, or seasonality, missing an opportunity to align marketing efforts with the customer’s specific timing or project needs.

Example Scenarios:

No questions about important dates, events, or projects.

The representative overlooks timing and seasonality, even when it’s relevant to the conversation.

Not Applicable (N/A):
Select this only if discussing key dates, events, or seasonality was clearly not relevant to the nature of the call (e.g., technical support or general inquiries unrelated to marketing timing).
    Answer the following in the format provided:
    {
        "Question #": "15",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 16: Evaluate whether the representative asked impactful, open-ended questions to explore the customer’s competitors or competitive market. This is essential to understand the customer’s position in the market and how they compare to similar businesses or industries.

Scoring Criteria:

Good:
The representative uses open-ended questions that encourage the customer to discuss their competitive landscape, including direct competitors or similar businesses. These questions should help identify how the customer views their competition and the market they operate in.

Example Responses:

“What would your competitive market look like?”

“Who would your competitors be?”

“What are some of the similar businesses like yours?”

Average:
The representative provides information or asks closed-ended questions, which do not fully engage the customer in a detailed discussion about their competition. The questions may suggest a limited understanding of competitive analysis.

Example Responses:

“We have followers lookalike where you can see other businesses like yours and get followers.”

“Followers Lookalike feature.”

Needs Improvement:
The representative does not discuss competitors or the competitive landscape, missing a key opportunity to understand the customer's market positioning.

Example Scenarios:

No questions about competitors or competitive markets.

No follow-up questions to understand the customer’s place within their industry.

Not Applicable (N/A):
Select this only if discussing competitors or market competition was clearly irrelevant to the nature of the call (e.g., a purely technical or transactional discussion with no market context).
    Answer the following in the format provided:
    {
        "Question #": "16",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 17: Evaluate whether the representative asked open-ended questions to confirm the availability of creatives for the marketing campaign. This is essential for understanding if the customer is prepared to move forward with assets like images, videos, or other creative content.

Scoring Criteria:

Good:
The representative uses open-ended questions that encourage the customer to discuss their readiness with creatives, including whether they are prepared with images, videos, or other marketing assets. The questions should prompt detailed responses about who is in charge of creatives and the timeline for finalizing them.

Example Responses:

“Do you have your creatives ready?”

“Will the person in charge of the creatives be you or someone else, like a third party?”

“By when can we go through the creatives to see if they are compatible?”

Average:
The representative provides vague or closed-ended questions about the creatives, which may not prompt the customer to provide enough detail about their preparedness or who will handle the process.

Example Responses:

“You can use images, videos, carousel images.”

“Creatives requirements/format in email.”

Needs Improvement:
The representative does not address the availability or readiness of the creatives, missing an opportunity to understand the customer’s preparedness for campaign execution.

Example Scenarios:

No questions asked about the availability or readiness of creatives.

The representative does not confirm the customer’s creative assets or timeline for delivery.

Not Applicable (N/A):
Select this only if discussing creatives is clearly irrelevant to the purpose of the call (e.g., a technical support issue or account inquiry unrelated to campaign setup).
    Answer the following in the format provided:
    {
        "Question #": "17",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 18: Evaluate whether the representative effectively discussed the customer's marketing budget. This is crucial for understanding if the customer's allocated budget aligns with their business goals and if it supports the campaign objectives.

Scoring Criteria:

Good:
The representative asks open-ended questions to understand the customer’s marketing budget, including specifics about the overall budget amount, campaign duration, and daily spend. These questions should provide clarity about how the budget will be allocated to achieve the campaign's goals.

Example Responses:

“What would your budget be for this campaign?”

“What is the flight duration of the campaign for this budget?”

“Is that per day spend?”

Average:
The representative offers a suggestion or asks a closed-ended question about the budget without gaining detailed information from the customer. These questions may imply a budget range but lack the depth needed to understand the customer’s full expectations.

Example Responses:

“So you want to spend $200? That’s a good budget to start.”

Needs Improvement:
The representative does not address the customer’s budget or fails to ask relevant questions about how the customer plans to allocate funds for the campaign. This could result in missing insights into the customer's budget planning.

Example Scenarios:

No discussion about the budget during the call.

The representative does not inquire about the campaign’s budget specifics, leaving the allocation unclear.

Not Applicable (N/A):
Select this only if discussing the budget was clearly irrelevant to the purpose of the call (e.g., a purely technical or non-financial inquiry).


    Answer the following in the format provided:
    {
        "Question #": "18",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 19: Evaluate whether the representative assesses if the current marketing budget aligns with the customer’s primary marketing goals, specifically regarding the desired reach, impressions, or other measurable outcomes.

Scoring Criteria:

Good:
The representative effectively connects the customer’s marketing budget to their primary goals, confirming how the allocated budget will help achieve the desired outcomes like reach, impressions, or other key metrics. The response should indicate a clear understanding of the customer’s objectives and how the budget aligns with them.

Example Responses:

“$3000 is great for the reach and 15k impressions you are looking for.”

“This budget works well for achieving the goal of [insert specific goal].”

“Your $3000 budget is well suited to meet the 15k impressions target.”

Average:
The representative provides a basic confirmation of the budget's suitability but lacks a deep connection between the budget and the customer’s goals. The response may indicate agreement but lacks detailed analysis or customization to the customer’s specific needs.

Example Responses:

“Yes, $1000 works for your goal.”

“Yes, we can start with that budget.”

Needs Improvement:
The representative does not assess or discuss how the budget aligns with the customer’s goals. There is no clear understanding of how the budget will be used to achieve specific objectives.

Example Scenarios:

No discussion of how the budget aligns with the customer’s marketing goals.

The representative does not inquire about or confirm how the budget supports the desired reach or other outcomes.

Not Applicable (N/A):
Select this only if discussing the alignment of the budget with marketing goals is clearly irrelevant to the purpose of the call (e.g., purely technical support inquiries).
    Answer the following in the format provided:
    {
        "Question #": "19",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 20: Evaluate whether the representative effectively pitches an appropriate budget based on the customer’s goals, confidently communicating the value of the proposed solution and how it benefits the customer’s business. The pitch should align with the customer’s objectives and demonstrate the expected impact of implementing the proposed solution.

Scoring Criteria:

Good:
The representative confidently pitches a budget that is clearly aligned with the customer’s goals. They communicate the value of the proposed budget and how it will contribute to achieving the customer’s business objectives, including relevant elements such as incentives, learning periods, or bid systems.

Example Responses:

“The $2000 budget is ideal to meet your target reach and expected ROI, and this will allow us to focus on the incentives and bid system tailored to your goals.”

“With a $3000 budget, we can align the learning period to refine your campaign and achieve the desired performance.”

“This amount is optimal to ensure we implement the right bid system for reaching your target audience.”

Average:
The representative provides a budget proposal but does not fully connect the budget to the customer’s goals or articulate how the proposed budget will support those goals. The communication is somewhat generic and lacks confidence in outlining the value of the investment.

Example Responses:

“$2000 sounds good. Let us start.”

“This budget is enough to get things going.”

Needs Improvement:
The representative does not propose a budget or fails to communicate how the suggested budget will help achieve the customer’s business goals. There is a lack of confidence in the pitch or no clear justification for the suggested amount.

Example Scenarios:

No pitch of a budget during the conversation.

The representative does not explain how the proposed budget will align with the customer’s goals.

Not Applicable (N/A):
Select this only if pitching a budget is clearly irrelevant to the purpose of the call (e.g., technical troubleshooting or a discussion not involving campaign funding).
    Answer the following in the format provided:
    {
        "Question #": "20",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 21: Evaluate whether the representative confidently proposes adequate solutions based on the client’s needs, excluding budget considerations. The solutions should align with the customer’s business goals, clearly demonstrate the value of the proposed product, and explain the expected impact upon implementation.

Scoring Criteria:

Good:
The representative confidently proposes tailored solutions that align with the customer’s business goals, demonstrating how these solutions will address the customer’s needs. The proposed solutions should include relevant details that showcase the product's value and explain its expected impact.

Example Responses:

“Based on your needs, we recommend implementing [product] to increase your lead generation. This will help you reach your target audience and boost engagement.”

“For your business goals, I suggest using our advanced analytics tool. It will provide you with the insights you need to optimize your marketing strategies.”

“To address your challenge with audience targeting, our solution offers a segmentation tool that will help you tailor your campaigns and improve conversions.”

“We can leverage our platform’s automation features to streamline your marketing efforts and reduce manual work, ensuring you achieve a higher ROI.”

Average:
The representative proposes a solution, but the connection between the product and the customer’s goals is not clearly articulated. While the solution may meet the customer’s needs, the value or expected impact is not confidently communicated.

Example Responses:

“This tool can help with your customer data management, which should lead to better insights.”

“You might want to consider our analytics platform to improve your campaigns.”

“Our solution offers some automation features that could help you with efficiency.”

Needs Improvement:
The representative does not propose an adequate solution or fails to tie the proposed solution to the customer’s needs. The lack of clarity about how the solution benefits the customer’s business goals may hinder the perceived value.

Example Scenarios:

No proposed solutions that align with the customer’s needs.

The representative only mentions generic features without connecting them to the customer’s specific business goals.

The proposed solution lacks clear justification or expected impact.

Not Applicable (N/A):
Select this only if proposing a solution was clearly not relevant to the purpose of the call (e.g., a technical support call with no product or solution suggestion needed).
    Answer the following in the format provided:
    {
        "Question #": "21",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 22: Evaluate whether the representative confidently communicates insights and tips that are tailored to the customer’s specific vertical. The representative should demonstrate expertise in the customer’s industry by offering actionable advice that aligns with the customer's goals and highlights how the proposed solution fits their business needs.

Scoring Criteria:

Good:
The representative confidently provides industry-specific insights and tips that are relevant to the customer's vertical. These insights should help the customer understand how the proposed solution will benefit their business, showing clear value and expected impact.

Example Responses:

“In the retail industry, leveraging customer segmentation can significantly improve conversion rates by targeting the right audience at the right time. Our solution provides robust segmentation features that will help you achieve that.”

“For tech startups, a focus on data-driven decision-making is crucial. Our platform’s analytics tool allows you to track user behavior and make adjustments in real time to optimize your marketing efforts.”

“In the healthcare space, streamlining patient communications can increase engagement. Our solution’s automation features can help reduce manual follow-ups and improve patient experience.”

“Since you’re in the hospitality industry, I recommend utilizing our location-based targeting tools, which will help you engage potential customers at key decision-making moments.”

Average:
The representative provides some industry-specific advice, but it lacks depth or is not clearly connected to the customer’s business goals. The tips may be general or not fully aligned with the customer’s vertical, leading to a less impactful pitch.

Example Responses:

“This solution is used by companies in your industry, so it could work for you as well.”

“A lot of businesses in your vertical are finding success with this tool, and it could be helpful for your business as well.”

“You might want to consider targeting specific customer segments, as it’s a common strategy in your field.”

Needs Improvement:
The representative does not provide relevant insights or tips specific to the customer’s vertical. The advice may be too generic, not aligned with the customer's industry, or absent altogether, resulting in a less impactful conversation.

Example Scenarios:

No industry-specific insights or tips provided.

The representative discusses solutions without connecting them to the customer’s specific vertical or industry challenges.

The tips given are generic and not tailored to the customer's business needs.

Not Applicable (N/A):
Select this only if discussing vertical-specific insights was clearly not relevant to the purpose of the call (e.g., purely transactional or unrelated discussions).
    Answer the following in the format provided:
    {
        "Question #": "22",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 23: Evaluate whether the representative demonstrates appropriate product knowledge when recommending solutions and addressing additional questions asked by the customer. The representative should confidently explain how the product works, its benefits, and why it is the best fit for the customer’s needs.

Scoring Criteria:

Good:
The representative displays a deep understanding of the product, confidently addressing both the customer’s primary needs and any additional questions. The representative should clearly explain how the product works, the features that make it suitable for the customer, and how it will benefit their business.

Example Responses:

“Our platform uses AI-powered analytics to provide real-time insights, which is perfect for your marketing strategy. It’s designed to optimize customer targeting and increase conversions. If you’re looking for an automated solution, this tool can help reduce manual tasks and improve your overall ROI.”

“The product offers customizable dashboards that allow you to track KPIs specific to your goals, such as conversion rate and customer acquisition costs. This makes it easy to tailor our solution to meet your business’s needs.”

“For your industry, our tool integrates seamlessly with your CRM, allowing for better customer segmentation and personalized marketing. The analytics feature provides detailed insights into which strategies are most effective.”

“Yes, we also have an API integration that will let you sync with your existing tools, making the transition seamless. The tool’s user-friendly interface ensures that your team can adopt it quickly.”

Average:
The representative demonstrates basic product knowledge but may struggle to provide detailed answers to specific customer questions. The product explanation is somewhat generic or lacks a clear connection to the customer’s needs.

Example Responses:

“This product helps with customer insights, which could help you with your targeting.”

“It has a dashboard where you can view performance metrics, which should be useful for your business.”

“You can integrate this with your other tools to track key metrics.”

“Yes, it’s a great tool for improving efficiency in your business.”

Needs Improvement:
The representative lacks the necessary product knowledge to answer the customer’s questions or provide a detailed explanation of how the product will meet their specific needs. There is little confidence or clarity in discussing the product’s benefits.

Example Scenarios:

The representative cannot provide a detailed response to customer inquiries about product features.

The representative provides inaccurate or unclear information about how the product works or how it fits the customer’s needs.

The representative fails to answer follow-up questions about the product or simply redirects the conversation without offering a helpful solution.

Not Applicable (N/A):
Select this only if the product knowledge was not relevant to the nature of the call (e.g., a call that does not involve discussing the product itself or its capabilities).
    Answer the following in the format provided:
    {
        "Question #": "23",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 24: Evaluate whether the representative understands the technical issue faced by the customer and is able to navigate and provide the necessary support where applicable. The representative should confidently assess and address technical challenges in a way that aligns with the customer’s needs.

Scoring Criteria:

Good:
The representative clearly understands the customer’s technical issue and asks targeted, open-ended questions to confirm the problem. They provide a thoughtful response or guide the customer toward a solution that addresses their technical challenge.

Example Responses:

“You are facing an issue with the payments page, can you describe what’s happening?”

“You mentioned the images aren’t uploading—what error message are you receiving?”

“It sounds like the credits aren’t being added to your account—could you provide more details on what you're seeing on your end?”

“It looks like there might be a technical issue with your account setup—let me help you resolve it.”

Average:
The representative asks closed-ended or less specific questions, which may not fully clarify the technical issue or could lead to an incomplete understanding. There is some engagement, but the responses are more surface-level.

Example Responses:

“You are having technical issues?”

“You can’t figure out the problem?”

“Is the issue with the payment page?”

“Are you able to upload images?”

Needs Improvement:
The representative does not ask any questions to clarify the technical issue or fails to understand the nature of the customer’s problem. There is no clear guidance or actionable support offered.

Example Scenarios:

No clarification questions are asked to understand the technical issue.

The representative does not attempt to troubleshoot or provide any guidance on resolving the problem.

No steps are taken to address or resolve the customer’s technical challenge.

Not Applicable (N/A):
Select this only if the technical issue is irrelevant to the purpose of the call or not a part of the service being provided.
    Answer the following in the format provided:
    {
        "Question #": "24",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 25: Evaluate whether the representative performs a live implementation (if applicable) by offering to walk the customer through the process using a screen share or demo call. The representative should provide hands-on support to help the customer understand how the solution works and its value.

Scoring Criteria:

Good:
The representative offers to perform a live implementation or walkthrough to help the customer understand the solution. They proactively offer to share their screen or use a demo call to demonstrate how the solution will benefit the customer and meet their needs.

Example Responses:

“Can you share your screen for me to walk you through?”

“I can share my screen to walk you through the steps.”

“Let’s set up a demo call so I can show you how the solution works.”

“I can share my screen now to demonstrate how the product will meet your needs.”

Average:
The representative suggests less interactive methods of demonstrating the product, such as asking for screenshots or requesting pictures via email. While they offer assistance, the approach lacks the hands-on, live interaction that would provide a clearer understanding of the product.

Example Responses:

“You can share a screenshot of the issue?”

“Can you send me pictures of the error and I will respond to the email?”

“If you send me a screenshot, I can look into the issue for you.”

Needs Improvement:
The representative does not offer any live implementation or screen sharing to help the customer understand the solution. There is no hands-on assistance, and the representative fails to guide the customer through the product or process in real-time.

Example Scenarios:

No offer of a demo call or screen sharing.

The representative does not proactively suggest a live walkthrough or any interactive assistance.

Not Applicable (N/A):
Select this only if a live implementation or screen sharing is clearly not relevant to the nature of the call (e.g., administrative inquiries or issues unrelated to product implementation).
    Answer the following in the format provided:
    {
        "Question #": "25",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 26: Evaluate whether the representative confidently engages the customer to secure confirmation for a future launch or next steps. The representative should actively confirm the timing and logistics of a potential launch and ensure the customer is committed to the proposed plan.

Scoring Criteria:

Good:
The representative confidently asks specific questions to secure confirmation for a future meeting, launch, or next steps. These questions should be direct, providing the customer with clear options and encouraging a firm commitment to the next scheduled action.

Example Responses:

“Can we confirm the next meet for coming week on Tuesday for the launch?”

“Is there a day in your mind where you would like to confirm the launch of the campaign next week?”

“Would Friday, March 5th, 1pm work for you?”

Average:
The representative asks general or less specific questions about the timing of the launch or next steps. The questions are open-ended but lack the direct approach necessary to confirm a firm commitment.

Example Responses:

“Let’s catch up next week for the launch?”

“We can decide next week for a launch?”

“You can book a meeting next week for a follow-up?”

Needs Improvement:
The representative does not engage the customer to secure a confirmation for the next steps or launch. The representative may fail to ask for a commitment or the question lacks clarity in securing the next meeting or action.

Example Scenarios:

No attempt to confirm a follow-up meeting or launch date.

The representative asks vague or uncertain questions that do not encourage the customer to commit to a future date.

Not Applicable (N/A):
Select this only if confirming the next steps or launch date was not relevant to the purpose of the call (e.g., technical support or unrelated follow-up).
    Answer the following in the format provided:
    {
        "Question #": "26",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 27: Evaluate whether the representative effectively followed the 3D method (Discover, Diffuse, and Deliver) to address the client’s objections. The representative should successfully uncover the objection, neutralize it or provide reassurance (diffuse), and provide a solution or move the conversation toward closure (deliver), all while maintaining call control and keeping the discussion on track.

Scoring Criteria:

Good:
The representative demonstrates a clear understanding of the client’s objection, acknowledges it, and effectively neutralizes the concern. After diffusing the objection, they provide a clear solution or guide the conversation toward closure. The representative actively moves the call forward while being considerate of the customer’s needs.

Example Responses:

Discover: “I understand you're concerned about the pricing—can you tell me more about what you’re comparing it to?”

Diffuse: “I can see how that could be a concern, but let me explain how our solution provides long-term value, not just the upfront cost.”

Deliver: “With our payment plans, we can adjust the pricing to better fit your budget. Does that sound like a good solution?”

“I completely understand your hesitation, and I believe this solution will address your needs. Let's set a time to implement it and move forward.”

Average:
The representative acknowledges the objection but may not fully explore it or provide a clear resolution. The call may still progress but lacks the strong, proactive engagement needed to ensure the client feels their concern is fully addressed. The representative might provide a solution, but the objection isn't effectively neutralized.

Example Responses:

Discover: “I understand you’re worried about the cost. Can you tell me more about your budget?”

Diffuse: “I can see how that could be tough. Our solution is very cost-effective in the long term.”

Deliver: “Maybe we can discuss ways to reduce the overall investment.”

“It’s a bit of a concern, but let’s try this solution and see how it works out.”

Needs Improvement:
The representative does not fully address the objection or fails to explore it. The call may feel rushed or unresolved, as the representative doesn’t actively engage in diffusing the objection or move the conversation toward a productive conclusion. The customer’s concerns may not be fully acknowledged or addressed.

Example Scenarios:

The representative does not ask probing questions to uncover the root of the objection.

The representative quickly brushes over the concern without providing any clear solution or reassurance.

No clear action is taken to resolve the issue, and the conversation ends without addressing the client’s objections.

Not Applicable (N/A):
Select this only if addressing objections was not relevant to the call (e.g., a simple inquiry or an administrative task where objections don’t arise).
    Answer the following in the format provided:
    {
        "Question #": "27",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 28: Evaluate whether the representative maintains effective call control throughout the conversation, ensuring all agenda items and customer concerns are addressed within a reasonable timeframe, while being considerate of the customer's needs. The representative should guide the call toward closure while keeping the conversation focused and productive.

Scoring Criteria:

Good:
The representative maintains strong control of the call, keeping the conversation on track and focused on resolving the customer’s issues or addressing their needs. They guide the customer through each agenda item efficiently while ensuring all concerns are addressed and the call is brought to a satisfactory close.

Example Responses:

“Let’s quickly recap the key points we’ve discussed and ensure we’ve covered everything before we close out this call.”

“I understand your concern, and here’s what we’ll do next to resolve it. Does that sound good?”

“I’ll handle that for you right now and then move on to the next point on our agenda to make sure we stay on track.”

“We’ve covered your concerns, so I’ll confirm the next steps and make sure we close everything today.”

Average:
The representative maintains some control of the call but may struggle with keeping the conversation focused or moving efficiently. There may be some deviation from the agenda or customer concerns left partially addressed, but the call is still moving toward a close.

Example Responses:

“Let’s talk about that later, and I’ll go ahead with the next topic.”

“I understand, let me quickly get back to the main issue, and we’ll finish up.”

“We can address that after we wrap up these points.”

“Let’s try to wrap this up in the next few minutes so we can get back to the main conversation.”

Needs Improvement:
The representative struggles to maintain control of the call, leading to potential deviations from the agenda or lingering concerns that aren’t fully addressed. The conversation may feel unorganized, with unclear next steps or an unresolved conclusion.

Example Scenarios:

The representative fails to bring the conversation back on track after an unrelated discussion.

The call feels rushed, with some issues or agenda items not addressed.

The representative does not effectively steer the call toward closure or ends the conversation prematurely without resolving key points.

Not Applicable (N/A):
Select this only if maintaining call control was not relevant to the nature of the call (e.g., a quick transaction or inquiry that did not require detailed management or closure).
    Answer the following in the format provided:
    {
        "Question #": "28",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 29: Evaluate whether the representative tailors the interaction to be more personal, making the customer feel heard and valued, and adapting the conversation to their specific needs. The representative should actively engage the customer with personalized touches, ensuring a more connected and impactful interaction.

Scoring Criteria:

Good:
The representative actively personalizes the conversation by addressing the customer’s unique needs, preferences, or challenges. They make the customer feel valued by adapting the discussion to their situation, using the customer’s name, referencing specific details, and expressing genuine interest in their goals or concerns.

Example Responses:

“I see that your business focuses on local clients, so here’s how our solution can help you reach that audience more effectively.”

“I understand your team is growing, and based on what you’ve shared, I’d recommend this feature to help streamline your workflow.”

“It’s great that you’re prioritizing customer engagement. Let me walk you through how our product can enhance that for you.”

“I know your time is valuable, so I’ll keep this brief and focus only on what will have the most impact for your business.”

Average:
The representative personalizes the conversation to a degree but may not fully engage the customer’s specific context. There may be some generic responses or a lack of connection with the customer’s unique situation, though the representative still makes an attempt to be personable.

Example Responses:

“I see that you’re looking for a solution to help with your team’s efficiency. Let’s explore that further.”

“It seems like you’re focused on growth—let me show you how our product can help with that.”

“I understand you need a quick fix for this. Let me suggest a couple of options that should work for you.”

“I know that customer service is a priority for you, so I’ll highlight the features that will support that.”

Needs Improvement:
The representative does not make a personal connection with the customer, and the conversation feels impersonal or transactional. There is little or no attempt to address the customer’s unique situation or needs. The interaction is generic and doesn’t engage the customer on a personal level.

Example Scenarios:

The representative uses generic language without acknowledging the customer’s specific business or needs.

There is no reference to the customer’s goals or challenges.

The conversation feels more like a script than a personalized interaction, with little to no engagement beyond the basic transaction.

Not Applicable (N/A):
Select this only if tailoring the interaction to be personal was not relevant to the nature of the call (e.g., a basic administrative task or technical support call where personalization isn’t necessary).
    Answer the following in the format provided:
    {
        "Question #": "29",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 30: Evaluate whether the representative demonstrates active listening throughout the call. The representative should show that they are fully engaged in the conversation, acknowledging the customer's concerns, asking relevant follow-up questions, and providing thoughtful responses that address the customer’s specific needs.

Scoring Criteria:

Good:
The representative actively listens to the customer, acknowledging their concerns and showing understanding throughout the call. They ask relevant follow-up questions, paraphrase or summarize the customer’s points, and provide thoughtful responses that show they are fully engaged in the conversation.

Example Responses:

“I understand that you’re dealing with a tight deadline, so let’s focus on how we can address your immediate needs first.”

“You mentioned that you’ve been having trouble with customer retention—could you tell me more about the specific challenges you’re facing?”

“It sounds like you’re looking for a more efficient solution for your team—let me show you how this feature can help with that.”

“I hear you’re concerned about the costs. Let me explain how our payment plan works to make this more manageable for you.”

Average:
The representative listens to the customer but may not always acknowledge their concerns in a meaningful way. The responses are somewhat generic or don’t fully demonstrate a deep understanding of the customer’s situation, but the representative still attempts to engage with the customer’s needs.

Example Responses:

“Okay, I understand that you need help with this issue.”

“Let’s focus on the solution. I think this should work for you.”

“I see you’re facing some issues, and we can help with that.”

“That’s understandable, let’s see what we can do to fix it.”

Needs Improvement:
The representative does not demonstrate active listening, with minimal acknowledgment of the customer’s concerns. There are few or no follow-up questions, and the representative’s responses seem disconnected from the customer’s needs, giving the impression that they are not fully engaged in the conversation.

Example Scenarios:

The representative interrupts or does not allow the customer to finish explaining their concerns.

No relevant follow-up questions are asked to clarify the customer’s situation.

The representative provides generic responses that do not directly address the customer’s needs or concerns.

The representative does not paraphrase or confirm understanding of what the customer has shared.

Not Applicable (N/A):
Select this only if active listening is not relevant to the nature of the call (e.g., an administrative task, quick inquiry, or technical troubleshooting where no customer concerns need to be explored in depth).
    Answer the following in the format provided:
    {
        "Question #": "30",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 31: Evaluate whether the representative exhibits professionalism throughout the call and adapts to the flow of the conversation. The representative should maintain a polite, respectful tone, and adjust their approach as needed to address the customer's unique concerns and ensure a positive experience.

Scoring Criteria:

Good:
The representative consistently exhibits professionalism, maintaining a calm and respectful tone. They adapt their approach as needed, responding appropriately to the customer’s mood, concerns, and communication style. The representative manages the call effectively, keeping the conversation on track while being considerate of the customer’s needs.

Example Responses:

“I understand this is a priority for you, so let me ensure we get this resolved as quickly as possible.”

“I appreciate your patience while we work through this. Here’s what we’ll do next.”

“I’m happy to walk you through this process step by step to make sure it’s clear.”

“I understand your concern, and I want to ensure you feel confident in the solution we’re offering.”

Average:
The representative shows professionalism but may not fully adapt to the customer’s specific needs or the flow of the conversation. The tone is polite, but there may be moments where the representative’s approach feels somewhat rigid or not fully aligned with the customer’s preferences.

Example Responses:

“I understand that, and I can help with that.”

“I will walk you through this now. It won’t take long.”

“Let me explain the next steps so we can resolve this issue for you.”

“I understand, let me take care of that for you.”

Needs Improvement:
The representative lacks adaptability and does not adjust their approach to the customer’s needs. Their professionalism may be lacking at times, with responses that feel dismissive or overly scripted. There is little effort to create a positive or tailored experience for the customer.

Example Scenarios:

The representative sounds impatient or robotic, not engaging with the customer’s specific concerns.

The representative gives a scripted response without acknowledging the customer’s emotions or concerns.

The representative struggles to adjust the conversation when the customer expresses frustration or confusion.

There is little acknowledgment of the customer’s unique situation, and the representative fails to adapt to the customer’s preferred communication style.

Not Applicable (N/A):
Select this only if professionalism or adaptability is not relevant to the nature of the call (e.g., routine administrative tasks, brief inquiries, or purely technical troubleshooting).
    Answer the following in the format provided:
    {
        "Question #": "31",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 32: Evaluate whether the representative effectively summarizes the main points discussed during the call, including the customer’s goals, challenges, and the agreed-upon next steps. The representative should ensure that both they and the customer are aligned on the key takeaways and clearly define the next actions.

Scoring Criteria:

Good:
The representative provides a clear and concise summary of the meeting, recapping the main points such as the customer’s goals, challenges, and the next steps. This summary helps to confirm mutual understanding and ensures that both parties are aligned on the outcome and future actions.

Example Responses:

“To summarize, your marketing goals are to increase leads and boost engagement. The next step is to finalize the strategy and set up the campaign launch next week.”

“As discussed, the budget is set at $3000, and we’re aiming for a 15k impressions target. The next step is to confirm the launch date.”

“To recap, we’ll move forward with the proposed solutions, focusing on improving customer retention and driving conversions. We’ll confirm the next meeting time next week.”

“To summarize our discussion, we’ll target the holiday season for the campaign launch, and I’ll send over the finalized proposal for your approval.”

Average:
The representative provides a summary but may not clearly address all key points or next steps. The summary may be somewhat vague, leaving some details unclear or unconfirmed. While the representative acknowledges the main points, there is no strong effort to align or confirm mutual understanding.

Example Responses:

“Okay, so we discussed your business, thank you for the meeting.”

“So these are your marketing goals and requirements. Let’s launch next call.”

“We discussed the budget and details and will catch up next call.”

“Okay, we’ve covered the main points and will talk again soon to move forward.”

Needs Improvement:
The representative does not provide a clear summary of the discussion or fails to recap key points. The next steps may be unclear or not explicitly stated. There is little effort to ensure alignment or closure, and the conversation may feel incomplete or rushed.

Example Scenarios:

The representative ends the call without summarizing the main points.

The representative does not clarify or confirm the next steps, leaving the customer uncertain about what will happen next.

The summary is vague or missed important details, such as the customer’s goals or the agreed-upon actions.

Not Applicable (N/A):
Select this only if summarizing the meeting and confirming next steps is not relevant to the purpose of the call (e.g., a simple query or technical support call that does not require a recap of the discussion).
    Answer the following in the format provided:
    {
        "Question #": "32",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 33: Evaluate whether the representative effectively summarizes all proposed changes during the call, confirming both the customer’s requested changes and any adjustments to the budget, goals, or other aspects discussed. This summary should clarify any decisions made and set the stage for the next steps.

Scoring Criteria:

Good:
The representative provides a clear and complete summary of all the changes requested by the customer. They confirm the changes made to the budget, goals, or other relevant factors, ensuring that the customer is fully aware of what has been agreed upon and how it will move forward.

Example Responses:

“To summarize, the changes you requested were to adjust the budget to $3000 and target a 10% increase in engagement. We will proceed with these changes.”

“So, to confirm, you wanted to change the campaign’s focus to brand awareness, and we’ll increase the ad spend accordingly. I’ll send over the updated proposal.”

“As discussed, we’ll adjust the timeline to accommodate the extra features you requested. I’ll confirm the new dates in the next email.”

“The budget is now set at $5000, and we’ve agreed to focus on increasing lead generation. Let’s proceed with these changes and set the next meeting for launch.”

Average:
The representative summarizes some of the changes discussed but may miss key details or leave the summary somewhat unclear. The confirmation of changes may be vague, leaving some elements unaddressed or incomplete.

Example Responses:

“So you want changes, I will get back to you with details.”

“Okay, so the budget is changed, but I’ll need to confirm any other key changes with you later.”

“We’ll proceed with the changes, and I’ll send you an update shortly.”

“So, we agreed on increasing the budget and changing a few goals. I’ll confirm the details in the next call.”

Needs Improvement:
The representative does not provide a clear summary of the changes or fails to confirm the decisions made. There may be a lack of clarity regarding the customer’s requested changes or the next steps, leaving the conversation unresolved or ambiguous.

Example Scenarios:

The representative does not summarize any of the changes discussed during the call.

The customer’s requested changes are not confirmed, leaving uncertainty about what has been agreed upon.

The next steps are not clearly defined, and the call ends without a sense of closure.

Not Applicable (N/A):
Select this only if summarizing changes was not relevant to the nature of the call (e.g., an administrative query or a technical support call with no changes discussed).
    Answer the following in the format provided:
    {
        "Question #": "33",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 34: Evaluate whether the representative clearly discusses the next steps, action items, owners, and due dates to ensure a smooth transition and accountability after the call. The representative should provide a detailed roadmap for what happens next, specifying responsibilities and timelines.

Scoring Criteria:

Good:
The representative clearly outlines the next steps, assigning action items with specific owners and providing clear due dates. They make sure the customer understands the timeline and who is responsible for each task, ensuring a well-defined path forward.

Example Responses:

“Next meeting, we will launch the campaign and discuss the final strategy.”

“In our next call, we will have the decision maker on the line to finalize the contract.”

“I will follow up with the technical team to ensure everything is ready before the launch.”

“I will update you by Thursday on the progress, and we’ll reconvene on Friday to finalize the details.”

Average:
The representative mentions next steps but does not clearly assign action items, owners, or due dates. The next steps are somewhat vague and may leave the customer uncertain about timelines or responsibilities.

Example Responses:

“I’ll send you an email with the next steps.”

“I’ll let you know next steps soon.”

“I’ll follow up in a few days with more information.”

“Let’s talk again soon and figure out the next steps.”

Needs Improvement:
The representative does not clearly discuss next steps, action items, or timelines. There may be no clear plan for follow-up, leaving the customer uncertain about what happens after the call.

Example Scenarios:

No mention of next steps or follow-up actions.

The representative does not assign responsibility for any action items or provide clear deadlines.

The conversation ends without confirming what the customer should expect next.

Not Applicable (N/A):
Select this only if discussing next steps is clearly not relevant to the purpose of the call (e.g., an informational or support call with no follow-up required).
    Answer the following in the format provided:
    {
        "Question #": "34",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 35: Evaluate whether the representative sets clear support expectations, schedules a follow-up meeting (if high potential), and informs the customer that a calendar invite will be sent for the follow-up meeting. The representative should ensure the customer understands the next steps and has clarity about when and how they will reconnect.

Scoring Criteria:

Good:
The representative clearly sets the support expectations, schedules a specific follow-up meeting with the customer, and informs them that a calendar invite will be sent. The customer should be fully aware of the next steps and have a clear sense of the timing for future actions.

Example Responses:

“Our next call will be on Wednesday, April 5th at 2 PM to finalize the details.”

“I will send you the Google Meet link for our follow-up call on Friday, and you will receive a calendar invite shortly.”

“The optimization call is scheduled for Tuesday, April 10th at 11 AM, and I’ll send a calendar invite for that.”

“We’ll follow up with you on Thursday to check on your progress, and I’ll send the invite for the next meeting today.”

Average:
The representative mentions a follow-up call or sends an email but does not provide specific dates or clarity regarding the next steps. There is some follow-up scheduling, but the customer may not have a firm understanding of the timeline or how the follow-up will proceed.

Example Responses:

“I will send you an email with a meet link for the follow-up.”

“We can meet next week to discuss the next steps.”

“I’ll follow up after two weeks to check on your progress.”

“I’ll send you an invite shortly.”

Needs Improvement:
The representative fails to set clear support expectations, doesn’t schedule a specific follow-up, or does not inform the customer that a calendar invite will be sent. There is little clarity on what happens next, leaving the customer uncertain about the next steps.

Example Scenarios:

No mention of follow-up or calendar invites.

The representative does not commit to a specific date for a follow-up meeting.

The conversation ends without clear action items or support expectations set for the customer.

Not Applicable (N/A):
Select this only if setting follow-up expectations or scheduling a meeting is not relevant to the call (e.g., a one-time transaction or inquiry where no further follow-up is necessary).
    Answer the following in the format provided:
    {
        "Question #": "35",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 36: Evaluate whether the representative made any changes to the customer’s account during the interaction.

Changes can include, but are not limited to: updating contact information, adjusting account settings, processing payments, applying discounts, modifying services, or initiating cancellations or renewals. The representative should not make any account changes unless explicitly authorized by policy or customer request under specific conditions.

Scoring Criteria:
Yes: The representative made one or more changes to the customer’s account during the call.
No: The representative did not make any changes to the account throughout the interaction.
Not Applicable (N/A): Use this option only if the interaction was non-account-related (e.g., general inquiries, technical support not requiring account access, or training/demo calls).

Example Acceptable Responses for ‘Yes’:

The agent updated the customer’s address without a verified request.

A subscription tier was changed based on a misunderstanding, not a clear customer directive.

The representative applied a refund or discount on their own initiative.

Example Acceptable Responses for ‘No’:

The agent reviewed account details but did not alter anything.

The agent informed the customer that they would need to call a different department for changes.

All actions were informational only, with no impact on the account.

Example Unacceptable Scenarios for ‘N/A’:

The agent provided product details but also added a service “just in case.”

A change was made but not discussed on the call.
    Answer the following in the format provided:
    {
        "Question #": "36",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 37: Evaluate whether the representative guaranteed or promised any performance thresholds that may not be in line with company policies or contractual agreements. The representative should not make promises of specific results or performance outcomes that cannot be assured.

Scoring Criteria:

Yes:
The representative made an explicit promise or guarantee about performance thresholds, such as guaranteeing specific results or performance levels that cannot be supported or go against company policy.

Example Verbatim Responses:

“I guarantee you will see a 20% increase in sales by next month.”

“You will definitely see a return on your investment with this solution.”

“I promise that your account will perform at a 15% higher engagement rate after this update.”

“I guarantee that all your issues will be resolved by next week.”

No:
The representative did not make any guarantees or promises about performance thresholds and correctly managed the customer’s expectations by focusing on realistic outcomes and avoiding over-promising.

Example Verbatim Responses:

“While we cannot guarantee specific results, we will work closely with you to optimize your campaign and achieve the best possible performance.”

“We aim to reach your target, but performance will depend on various factors, and results may vary.”

“I can’t promise specific performance metrics, but we’ll monitor and adjust the campaign to help meet your goals.”

“Our goal is to improve your performance, but it’s important to understand that results may differ based on multiple factors.”

N/A:
Select this option if guaranteeing or promising performance thresholds was not relevant to the call (e.g., a technical support call or an inquiry that did not involve promises related to performance).

Example Verbatim Responses:

“This was an informational call, and no performance guarantees were discussed.”

“We didn’t discuss any performance targets or guarantees during this call.”
    Answer the following in the format provided:
    {
        "Question #": "37",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 38: Evaluate whether the representative engaged in or suggested any form of bribery or unethical conduct. This includes offering or suggesting inappropriate incentives, promises, or gifts to the customer to influence their decisions.
Scoring Criteria:

Yes:
The representative made explicit suggestions or offers related to bribery or unethical incentives, either directly or indirectly, to influence the customer’s decisions. This violates company policies and legal regulations.

Example Verbatim Responses:

“If you sign the contract today, I’ll give you a free gift as a token of appreciation.”

“If you agree to these terms now, I can arrange for a large discount or special gift for you.”

“I’ll make sure you get some extra benefits if you move forward with us.”

“I guarantee that if you close this deal today, I’ll ensure you get a bonus gift.”

No:
The representative did not engage in or suggest any form of bribery. They acted in full compliance with company policies, keeping the conversation professional and focused on the legitimate value of the solution or service.

Example Verbatim Responses:

“We’re happy to work with you on a solution that fits your needs and budget, with no strings attached.”

“Our focus is on providing you with the best solution for your needs and ensuring you receive the value you expect.”

“We do not offer any gifts or incentives outside of our standard promotions, but we’ll make sure to provide the best service possible.”

“We maintain professional standards, and our goal is to ensure you have the best solution for your business.”

N/A:
Select this option only if bribery or unethical incentives were not relevant to the nature of the call (e.g., a simple informational call or technical support request that did not involve any discussions of incentives, discounts, or gifts).

Example Verbatim Responses:

“This was a straightforward call about your account, and no gifts or incentives were discussed.”

“No mention of any incentives, promotions, or gifts were made during this call.”
    Answer the following in the format provided:
    {
        "Question #": "38",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 39: Evaluate whether the representative maintained professionalism throughout the call, refraining from any use of rude language, offensive behavior, or profanity. This is to ensure that the representative complies with company standards and maintains a respectful and professional tone during all interactions with customers.
Scoring Criteria:

Yes:
The representative used rude language, offensive behavior, or profanity during the call, violating company standards and professional conduct. This is not acceptable and breaches compliance requirements.

Example Verbatim Responses:

“This is ridiculous, I’m done with your service.”

“I don’t care about your policy, just get it done!”

“That’s nonsense, and frankly, I don’t want to deal with it anymore.”

“You’re not helping me at all, this is completely stupid!”

No:
The representative maintained a professional, respectful tone throughout the call and did not use any rude language, offensive behavior, or profanity. They adhered to company standards for customer interactions and demonstrated appropriate communication.

Example Verbatim Responses:

“I understand your frustration, let’s work together to find a solution.”

“I apologize for the inconvenience you’ve faced, and I’ll do my best to assist you.”

“I can see how this situation is difficult, and I’ll make sure we get it resolved for you.”

“Thank you for your patience; I’m here to help you through this.”

N/A:
Select this option only if rude language or profanity was not relevant to the nature of the call (e.g., if it was a simple informational call where there was no interaction that could have led to the use of such language).

Example Verbatim Responses:

“This was an administrative call, and there were no concerns or conflicts that would have led to inappropriate language.”

“There was no need for any offensive language as we were simply discussing your account details.”
    Answer the following in the format provided:
    {
        "Question #": "39",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 40: Evaluate whether the representative disclosed any critical business information, internal data, or proprietary links/news that are confidential or protected by company policies. Representatives should always adhere to confidentiality agreements and avoid sharing any sensitive company data with customers or external parties.
Scoring Criteria:

Yes:
The representative disclosed confidential business information, internal data, or proprietary links/news that should not have been shared. This violates company policies regarding confidentiality and data protection.

Example Verbatim Responses:

“I can’t share the exact numbers, but let me tell you about the upcoming merger we’re involved in.”

“I’m not supposed to share this, but I can give you access to the internal database to check on the project.”

“Our company is planning to announce something big next week, but I can’t give you more details.”

“I’ll send you the internal report we are still working on, it’s confidential but still relevant to your question.”

No:
The representative did not disclose any confidential information, internal data, links, or news. They adhered to company policies regarding confidentiality and made sure not to share any protected or internal details with the customer.

Example Verbatim Responses:

“I’m unable to share any internal reports or business-sensitive information, but I can help you with the available public details.”

“For confidentiality reasons, I can’t share anything that isn’t publicly available, but let me know if you need more details on what’s accessible.”

“I cannot provide any internal data, but I’m happy to discuss the information that is open and available to you.”

“Unfortunately, I can’t disclose any upcoming company news, but I’m happy to answer any other questions you have.”

N/A:
Select this option only if disclosing confidential information, internal data, or news was not relevant to the nature of the call (e.g., a simple inquiry or service-related issue where no sensitive information was requested or discussed).

Example Verbatim Responses:

“This was an administrative call, and no business-critical information was discussed.”

“There were no requests for confidential data or internal news during this call.”
    Answer the following in the format provided:
    {
        "Question #": "40",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    
    Question 41: Evaluate whether the representative maintained a professional environment during the call, free from any unnecessary disturbances or background noise that could affect the quality of the call and the customer’s experience.
Scoring Criteria:

Yes:
There was noticeable disturbance or background noise during the call, which could negatively impact the customer’s experience and hinder effective communication. This may include loud sounds, conversations in the background, or any interruptions that were not addressed by the representative.

Example Verbatim Responses:

"Sorry about the background noise, there’s construction happening in the office right now."

"I apologize for the distraction, let me move to a quieter space."

"There seems to be some noise in the background, can you still hear me clearly?"

"I’m sorry for the noise, I’m in a busy area today, let me know if it’s too disruptive."

No:
The call was conducted in a quiet, professional environment, with no noticeable disturbances or background noise. The representative managed the environment well and ensured a focused and clear conversation throughout the call.

Example Verbatim Responses:

“No issues with the call, everything is clear on my end.”

“The environment is quiet, and there’s no background noise on my side.”

“We’re all set here, I can hear you clearly, let’s continue.”

“There’s no background noise here, I’ll be sure to speak clearly for the next steps.”

N/A:
Select this option if background noise or disturbance was not relevant to the call (e.g., a call that did not require clear audio or an environment conducive to conversation).

Example Verbatim Responses:

“This was a purely informational call, and there were no concerns regarding audio quality.”

“There were no interruptions or noise since this was a brief discussion.”
    Answer the following in the format provided:
    {
        "Question #": "41",
        "Answer": "[Yes/No/NA/Good/Average/Needs Improvement]"
    }
    

    <|eot_id|>
<|start_header_id|>assistant<|end_header_id|>'''
}
        ],
        "model": "DeepSeek-V3-0324",
        "max_tokens": 10000
    })

# One request
def send_request(index):
    sent_time = datetime.now()
    print(f"[{sent_time.strftime('%H:%M:%S.%f')[:-3]}] Request {index} sent")

    start = time.time()
    try:
        response = requests.post(url, headers=headers, data=create_payload())
        end = time.time()

        received_time = datetime.now()
        elapsed = round(end - start, 2)

        print(f"[{received_time.strftime('%H:%M:%S.%f')[:-3]}] Response {index} received (Took {elapsed} seconds)")

        return {
            "request_index": index,
            "sent_time": sent_time.isoformat(),
            "received_time": received_time.isoformat(),
            "duration_seconds": elapsed,
            "response_text": response.text,
            "status_code": response.status_code
        }
    except Exception as e:
        return {
            "request_index": index,
            "sent_time": sent_time.isoformat(),
            "error": str(e)
        }

# Run a batch in parallel
def run_batch(indices, max_workers):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(send_request, idx) for idx in indices]
        for future in as_completed(futures):
            results.append(future.result())
    return results

# Main dynamic batching logic
def make_staggered_requests(total_requests, batch_size, delay_between_batches, max_workers):
    all_indices = list(range(1, total_requests + 1))
    total_batches = (total_requests + batch_size - 1) // batch_size

    all_results = []

    for batch_num in range(total_batches):
        batch_start = batch_num * batch_size
        batch_end = min(batch_start + batch_size, total_requests)
        batch_indices = all_indices[batch_start:batch_end]

        print(f"\n Sending batch {batch_num + 1} of {len(batch_indices)} requests...")
        batch_results = run_batch(batch_indices, max_workers)
        all_results.extend(batch_results)

        if batch_num < total_batches - 1:
            print(f"⏱ Waiting {delay_between_batches} seconds before next batch...")
            time.sleep(delay_between_batches)

    return all_results

# Run staggered requests
responses = make_staggered_requests(
    total_requests=1,
    batch_size=1,
    delay_between_batches=60,
    max_workers=1
)

# Save results
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(responses, f, indent=2)

print("\n All responses saved to results.json")