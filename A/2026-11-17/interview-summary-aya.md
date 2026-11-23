# Inverted Interview — Summary (Aya)
*Under Your Skin · From Play to Prevention · 2026-11-17*
*To share with Raimundo and Maurice. Each of us runs the same interview and we compare the three summaries.*

The full round-by-round log is in `2026-11-17-inverted-interview.md`.

---

## 1. What I gave the tutor (inputs)

**The interview prompt** (`2026-11-17-prompt-ai-general.md`)
The tutor plays an interaction design tutor running an inverted interview: 1–2 questions at a time, plain language, separating what we observed from what we assume, letting us say "we don't know yet", asking before proposing solutions, and not assuming AI has to be in the game. It ends by asking whether we're ready for a Working Project Definition.

**General notes — 10 Nov** (`2026-11-10-notes.txt`)
Organised feedback from Mariana, Zoé, Juliana, Douglass, Maurice and the group discussion:
- *Mariana:* use ordinary, relatable incidents; cyberbullying often starts at school and continues online; don't make the account a monster; roles blur between victim and perpetrator; possible win condition = people stop feeding the account; research school meme / confession / crush accounts.
- *Zoé:* online, you don't see the other person's reaction (digital distance); the account as a black box; "when does it stop being funny?"; harassment comes from repetition and many people joining in; turning points that reduce emotional distance; possible escalation towards deepfakes; reference to Emmanuelle Piquet.
- *Juliana:* players should experience their own complicity (liking, sharing, laughing, staying silent).
- *Douglass:* what if people feed the account positive content?
- *Maurice:* the account as intermediary, so who is responsible when harm passes through several layers?
- Retained decisions: no monster; algorithmic AI account; ordinary starting incident; everyone potentially complicit; uncomfortable ending allowed; explore algorithmic amplification; don't glorify or teach harassment.
- 7-chapter outline, an action/consequence table, 4 possible endings (collective withdrawal, continued escalation, intervention, redirecting the system), ethical principles, 11 open questions, next steps (ethnography, talk to teens, choose the incident, prototype 7 posts…).

**Concept — 17 Nov** (`2026-11-17-concept.md`)
"When a Joke Doesn't End". Not seven acts of bullying but one act that never ends. Mechanism: the joke survives because people keep laughing. Seven transformations of the same moment: Meme → Sticker → AI Remix → Reenactment → Running Joke → "It's Not Funny Anymore" → "Does It Ever Stop?" (stages 5–7 are suggested, 1–4 come from our notes). Four lessons: repetition changes meaning; the group gives harassment its power; where you stand changes how it feels; the first person to say "not funny" is challenging the group. Left open: the exact incident, how interactive it is, platform and point of view. Design test: *does this show the same joke gaining power through repetition, transformation or people joining in?*

**Pitch — 17 Nov** (`2026-11-17-pitch.txt`)
Title *Under Your Skin* (Raimundo, Aya, Maurice). Same story told more tightly. Two personas:
- **Lovely_Croissant** (13, ~12 h online): indecisive, seeks validation, sidekick of the popular girl; joins in because everyone laughs, even when uncomfortable.
- **3EYEx** (13, ~8 h online): conspiracy-minded, curious, fixated (Dipper-like); investigates who started the joke and misses that the whole school, himself included, keeps it alive.

---

## 2. What the tutor gave me back

**Its reading of our material**
- *Settled:* the core idea, the seven-transformation backbone, the design test, the ethical principles, the two personas.
- *Observed:* feedback from tutors and classmates and the group discussion.
- *Not yet observed:* talks with 12–16-year-olds, the meme-account ethnography, any playtest. So "players will recognise their complicity" is still an assumption.

**Tensions it pointed out**
1. The 10 Nov notes centre an anonymous algorithmic account; the 17 Nov pitch barely mentions it.
2. Both personas are classmates, and nobody had said who the *player* is.
3. Seven chapters vs. the length of a short playable experience.
4. (Later) A 4-stage prototype stops before the moment where choices are meant to matter.
5. (Later) Complicity is the pitch's central aim but wasn't among my playtest priorities.

**How it worked**
After the first open question I asked for options, so from then on each question came with 3–4 proposals plus "don't know yet". **Important for comparing:** the tutor wrote those options, so they shaped my answers. Raimundo and Maurice could answer the questions in section 5 openly first, before looking at options.

---

## 3. My answers / decisions so far

| # | Question | Options offered | My answer |
|---|---|---|---|
| 1 | Most urgent thing to settle for Phase II | Who the player is / what the player does / interface / prototype scope | **Who the player is** |
| 2 | Who does the player play? | One classmate / switching views / the crowd / the target | **Switching views** |
| 3 | What triggers a switch? | One view per stage / follow the joke / player chooses / don't know | **One view per stage** |
| 4 | How close to the target? | Never their view / last view only / someone close / don't know | **Open**: I lean towards "never their view" (only traces) but want input from teens / research partners |
| 5 | Main action in each view | React to posts / reply in a chat / decide to pass it on / don't know | **React to posts + reply in chats** |
| 6 | Do actions change the joke's growth? | Linear / small traces only / changes the ending / don't know | **Traces + changes the ending** |
| 7 | Interface | Phone mockup / fictional platform / mixed media / don't know | **Fictional platform** (invented app, not TikTok/Insta) |
| 8 | Can the player see the joke growing? | Counter / indirect signs / hidden until end / don't know | **Counter + indirect signs** |
| 9 | Role of the AI account | Central / background / dropped / don't know | **Dropped** |
| 10 | Prototype tool | HTML/CSS/JS / p5.js / Twine-Ink / Figma-paper | **HTML/CSS/JS**, all content scripted, no real AI |
| 11 | Prototype size | 3 stages / 4 stages / all 7 rough / don't know | **4 stages** |
| 12 | How the target and the moment are shown | Illustrated / abstract-blurred / stylised photos / don't know | **Illustrated** |
| 13 | How the 4-stage prototype ends | Recap screen / short stage 5 / open ending + talk / don't know | **Short stage 5** ("It's not funny anymore") |
| 14 | First playtest: what to learn | Feel complicit? / believable? / push the counter? / sense the target? | **Believable + push the counter + sense the target**, and later **complicit** added as something to experiment with |

---

## 4. Tutor's notes on my answers (to discuss)

- **Switching views + choices adding up = the player *is* the crowd.** One player controls each classmate in turn, so their combined choices are "the group". Stage 5 could show the player that the crowd keeping the joke alive was them. This could be the main prevention moment.
- **One view per stage → 4–5 characters needed.** Only 2 personas exist so far.
- **Counter risk:** a visible number can turn into a score to beat. If players push it "for fun", that's a real insight, but the debrief has to deal with it.
- **Fictional platform:** needs its own name, look and conventions, and must still read as social media to 12–16-year-olds (to check with the ethnography / teens).
- **Dropping the account** removes the "black box / who is responsible" layer (Zoé, Maurice) and makes "people keep it alive" clearer. The AI remix can still appear as a format at stage 3, made by a classmate, not by a system.
- **Illustration** lets memes and stickers exaggerate the moment without using a real person's image.
- **Understanding vs. complicity.** My instinct: players don't necessarily need to *feel* complicit to *understand* how the joke evolves. The pitch leans towards complicity ("confronted with their own role"). Possible test: a stage 5 recap that names the player's actions ("you shared it 3 times") vs. one that only shows the joke's path through the school.

---

## 5. Where things stand

**Established (my version)**
- Situation: one small school moment becomes collective humiliation because the group keeps it alive.
- Player: switches views, one classmate per stage.
- Actions: react to posts + reply in group chats.
- Consequences: choices come back as traces and add up to shape stage 5.
- Interface: fictional platform; counter + indirect signs.
- No AI account; HTML/CSS/JS; scripted content; illustrated.
- First prototype: stages 1–4 + short stage 5.

**Still open**
- The exact incident (to choose with teens).
- How close we get to the target.
- Extra characters beyond the 2 personas.
- Name and look of the fictional platform.
- The tipping rule: how choices add up, and how many it takes to change stage 5.
- Aim: understanding the mechanism vs. recognising one's own role.
- Care: what (if anything) is stored; facilitation and debrief; what happens if a player recognises their own situation.
- Device and setting: phone vs. classroom laptop; alone, in pairs, or as a class.

**Proposed next steps (from the tutor, not decided)**
1. Compare our three summaries and decide together.
2. Draft a Working Project Definition (1–2 pages, open questions included).
3. Write the stage script (views, posts, chats, choices).
4. Sketch the fictional platform (name, feed, chat).
5. Build the HTML/CSS/JS prototype.
6. Playtest with 12–16-year-olds.

---

## 6. For Raimundo and Maurice: questions to answer before comparing

*Try answering in your own words first, then look at the options in section 3.*

1. What is our proposal, and what do we most need to clarify?
2. Who does the player play?
3. If several views: what moves the player from one to the next?
4. How close does the player get to the target?
5. What does the player do in each view?
6. Do their actions change what happens?
7. What does the player see (interface/platform)?
8. Can they see the joke growing while playing?
9. Do we keep the anonymous AI account?
10. What do we build the first prototype with?
11. How big is the first prototype?
12. How are the target and the moment shown?
13. How does the prototype end?
14. What should the first playtest tell us?
15. Is the aim to understand how the joke spreads, or to recognise our own role in it, or both?

<!-- nav:footer -->

---

↑ [Home](../README.md) · [A](README.md)

<!-- /nav:footer -->
