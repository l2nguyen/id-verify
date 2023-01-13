## Description
This branch is an example Rasa 3.x bot that includes logic to make the user verify something at the start of the conversation before continuing with the use case.

In the case of this simple example, the user has to agree to a data privacy policy before continuing. This can be extended for a more complex authentication.

This has the following:

- a form (ds_form). This form might be changed to actually perform authentication, or it might just complete silently having verified that the user is authenticated.
- The goal action of the original intent run in the custom action [action_start_convo](actions/actions.py)

There are rules that run the form and pick up at the submission of the form and run a follow up action.

For the first question in the form, there is a welcome. But his could also be a custom payload  / empty message / something you hide on the frontend.

```yaml
  utter_ask_init_message:
  - text: "hello, how can I help you?"
```


Here's what the conversation looks like with a modified moodbot:
```bash
Bot loaded. Type a message and press enter (use '/stop' to exit): 
Your input ->  /$chat_start                                                                                     
hello, how can I help you?
Your input ->  i am sad                                                                                         
Before I can help you, do you agree to our data privacy policy?
Your input ->  yes                                                                                              
Here is something to cheer you up:
Image: https://i.imgur.com/nGF1K8f.jpg
Did that help you?
```

If the user does not agree to the policy:

```bash
Your input ->  /$chat_start                                                                                     
hello, how can I help you?
Your input ->  are you a bot?                                                                                   
Before I can help you, do you agree to our data privacy policy?
Your input ->  no                                                                                               
Sorry, I am unable help you with this if you do not agree to the data privacy policy
```
