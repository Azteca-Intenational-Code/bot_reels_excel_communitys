from openai import OpenAI
from dotenv.main import load_dotenv
import os
import random

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class GPT:
    def __init__(self, design_data):
        self.client = OpenAI()
        self.services = design_data.get("service").split(", ")
        self.service = random.choice(self.services)
        self.campaign = design_data.get("campaign")
        self.lang = design_data.get("lang")
        self.SYSTEM_MESSAGE = f"As a system, you can generate eye-catching content for social networks. Always respond in {self.lang}"
        self.ASSISTANT_MESSAGE = "As an assistant you will be a community manager who will help me generate eye-catching content for social media. Do not add any opinion, just follow the instructions."

    def create_message(self, role, content):
        return {"role": role, "content": content}

    def generate_response(self, model, messages, temperature=1):
        response = self.client.chat.completions.create(
            model=model, messages=messages, temperature=temperature
        )
        res = response.choices[0].message.content
        clean_response = (
            res.replace("'", " ")
            .replace("\n", " ")
            .replace("```html", " ")
            .replace("```", " ")
        )
        return clean_response

    # ============================= OSCEOLA METHODS ==============================

    def copy_osceola(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate compelling copy for {theme}. The copy should include a catchy hook, key benefits of the service, a clear call to action and two strategic emojis at the end of the copy. Additionally, create 10 hashtags that are viral and eye-catching with the information in the copy. The copy should be {characters} characters long.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def theme_osceola(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {self.service}, provide a theme that captures the essence of the service. The theme should be engaging, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def document_title_osceola(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {theme}, provide a single word that best represents an important characteristic or benefit of this service. The word should be concise, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def youtube_video_title_osceola(self, theme, characters=40):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Give me a YouTube title with a catchy word in all caps and emoji at the end for: {theme} and the title should be {characters} characters long",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def youtube_video_tags_osceola(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a list of relevant YouTube tags for the following service: {theme}. Tags should relate to the service's benefits, features, location in Chicago, and common search terms used by potential customers. Provide a mix of general and specific keywords to maximize visibility, separated by commas, should be ten words.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def first_comment_osceola(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        prompt_hashtags_only = f"""
        You are Osceola Fence — a fence manufacturing and installation company in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Osceola Fence account** — not a viewer.

        ✳️ Style: Hashtags only.
        - Leave two blank lines at the top.
        - Then insert either 👇👇👇 or … on a single line.
        - On the next line, write 3–4 original, professional hashtags about fencing, security, custom installations, or Chicago.
        - Do **not** use emojis or regular text (except 👇👇👇 or …).
        - Avoid generic combos like #SecureHome or #FenceGoals — create varied, rotating tags.

        ✅ Max {characters} characters.
        ✅ Must feel like a branded, professional comment.
        ✅ Make hashtags fresh and non-repetitive.
        """

        prompt_statement_plus_hashtags = f"""
        You are Osceola Fence — a fence manufacturing and installation company in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Osceola Fence account** — not a viewer.

        ✳️ Style: Statement + hashtags.
        - Begin with a short, confident sentence in first person plural (e.g., "We make your perimeter stronger." or "Our team delivers precision every time.").
        - Maintain a serious but friendly tone.
        - Add 1–2 rotating, professional hashtags at the end.
        - Use **only one emoji** if relevant, and vary it in each version.

        ✅ Max {characters} characters.
        ✅ Do not include links.
        ✅ Must sound professional and real.
        """

        prompt_direct_text = f"""
        You are Osceola Fence — a fence manufacturing and installation company in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Osceola Fence account** — not a viewer.

        ✳️ Style: Short direct message.
        - Use a single clean sentence in first person plural.
        - Keep tone confident, professional, and human.
        - No hashtags, no links.
        - One emoji allowed if it adds value — vary it each time.

        ✅ Max {characters} characters.
        ✅ Avoid repetition or generic phrasing like "we’re here for you."
        """

        estilos = [
            prompt_hashtags_only,
            prompt_statement_plus_hashtags,
            prompt_direct_text
        ]

        selected_prompt = random.choice(estilos)
        user_message = self.create_message("user", selected_prompt)

        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).strip('"')


    def tikTok_title_osceola(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a catchy TikTok title for the following service: {theme}. The title should include a strong keyword, be attractive and end with a relevant emoji only at the end of the comment, and be {characters} in length, without hashtags.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")

    # ============================= QUICK CLEANING METHODS ==============================

    def copy_quick_cleaning(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a compelling copy for {theme}. The copy should include a catchy hook, key benefits of the service, and two strategic emojis at the end of the text. Additionally, create 8 viral and eye-catching hashtags based on the information in the copy. The copy should be {characters} characters long.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")
    
    def theme_quick_cleaning(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {self.service}, provide a theme that captures the essence of the service. The theme should be engaging, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def document_title_quick_cleaning(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {theme}, provide a single word that best represents an important characteristic or benefit of this service. The word should be concise, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def youtube_video_title_quick_cleaning(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Give me a YouTube title with a catchy word in all caps and emoji at the end for: {theme} and the title should be {characters} characters long",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def youtube_video_tags_quick_cleaning(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate 10 short, relevant YouTube tags for {theme}, focusing on its quick and cost-effective benefits. Tags should be a combination of general and specific keywords, each separated by commas. Remember to do not include enumerations and hashtags.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def first_comment_quick_cleaning(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        prompt_hashtags_only = f"""
        You are Quick Cleaning — a cleaning company in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Quick Cleaning account** — not a viewer.

        ✳️ Style: Hashtags only.
        - Leave two blank lines at the top.
        - Then insert either 👇👇👇 or … on a single line.
        - On the next line, write 3–4 original, rotating hashtags about cleaning, move-outs, freshness, etc.
        - Avoid common combos like #FreshStart + #SparklingClean. Make them sound new.
        - Do **not** include any text or emojis (except 👇👇👇 or …).
        
        ✅ Max {characters} characters.
        ✅ Must look like it was written by Quick Cleaning.
        ✅ Make sure hashtags are fresh and different each time.
        """

        prompt_question_plus_hashtags = f"""
        You are Quick Cleaning — a cleaning company in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Quick Cleaning account** — not a viewer.

        ✳️ Style: Question + hashtags.
        - Begin with a **creative and unusual question** in first person plural (e.g., "Need help with the moving chaos?" or "Tired of the packing mess?").
        - The tone should rotate between funny, helpful, urgent, or casual.
        - Add 1–2 rotating hashtags at the end.
        - One emoji max, and not the same each time.
        - Avoid phrases like "fresh start" or "sparkling clean" — use new wording.

        ✅ Max {characters} characters.
        ✅ Do not use links.
        ✅ Must feel dynamic and different on every use.
        """

        prompt_direct_call_to_action = f"""
        You are Quick Cleaning — a cleaning company in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Quick Cleaning account** — not a viewer.

        ✳️ Style: Direct call to action.
        - Write a short, **highly varied CTA** using first person plural.
        - Every version should feel different: some can be direct, others playful or energetic.
        - Use **only one emoji**, and vary it each time.
        - Do not include hashtags or links.
        - Avoid repeating phrases like "let us handle it" or "we’ve got your back".

        ✅ Max {characters} characters.
        ✅ Must sound like a real brand post — unique and informal.
        """

        estilos = [
            prompt_hashtags_only,
            prompt_question_plus_hashtags,
            prompt_direct_call_to_action
        ]

        selected_prompt = random.choice(estilos)
        user_message = self.create_message("user", selected_prompt)

        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).strip('"')

    def tikTok_title_quick_cleaning(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a catchy TikTok title for the following service: {theme}. The title should include a strong keyword, be attractive and end with a relevant emoji only at the end of the comment, and be {characters} in length, without hashtags.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    # ============================= ELITE SPA METHODS ==============================
    
    def copy_elite_spa(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a compelling copy {theme}. The copy should include a catchy hook, key benefits of the service, and two strategic emojis at the end of the text. Additionally, create 8 viral and eye-catching hashtags based on the information in the copy. The copy should be {characters} characters long.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def theme_elite_spa(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {self.service}, provide a theme that captures the essence of the service. The theme should be engaging, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def document_title_elite_spa(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {theme}, provide a single word that best represents an important characteristic or benefit of this service. The word should be concise, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def youtube_video_title_elite_spa(self, theme, characters=40):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE) 
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a catchy title for a short video about {theme}. The title should be engaging, relevant, and impactful. It should be {characters} characters long.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def youtube_video_tags_elite_spa(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a list of relevant YouTube tags for the following service: {theme}. Tags should relate to the service's benefits, features, location in Chicago, and common search terms used by potential customers. Provide a mix of general and specific keywords to maximize visibility, separated by commas, should be ten words.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def first_comment_elite_spa(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        prompt_hashtags_only = f"""
        You are Elite Chicago Spa — a spa focused on wellness, beauty, and self-care.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Elite Chicago Spa account** — not a viewer.

        ✳️ Style: Hashtags only.
        - Leave two blank lines at the top.
        - Then insert either 👇👇👇 or … on a single line.
        - On the next line, write 3–4 soft, elegant hashtags related to relaxation, skincare, wellness, and spa lifestyle.
        - Do **not** use emojis or regular text (except 👇👇👇 or …).
        - Avoid cliché combos like #SelfCareSunday — invent new, fresh expressions.

        ✅ Max {characters} characters.
        ✅ Make sure hashtags rotate and feel brand-consistent.
        """

        prompt_phrase_plus_hashtags = f"""
        You are Elite Chicago Spa — a spa focused on wellness, beauty, and self-care.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Elite Chicago Spa account** — not a viewer.

        ✳️ Style: Gentle phrase + hashtags.
        - Start with a warm, caring sentence in first person plural (e.g., “We love creating calm in every session.”).
        - Keep the tone soft, elegant, and nurturing.
        - Add 1–2 rotating hashtags related to spa, skin, or relaxation.
        - You may include **only one emoji**, and vary it each time.

        ✅ Max {characters} characters.
        ✅ No links. Avoid repetition.
        """

        prompt_soft_text_only = f"""
        You are Elite Chicago Spa — a spa focused on wellness, beauty, and self-care.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Elite Chicago Spa account** — not a viewer.

        ✳️ Style: Soft text only.
        - Use first person plural voice (we/our).
        - Write a short, nurturing sentence that communicates beauty, care, or peace.
        - Do **not** include hashtags or links.
        - Add one soft emoji if it enhances the message — vary it for each version.

        ✅ Max {characters} characters.
        ✅ The tone must feel premium, calm, and authentic.
        """

        estilos = [
            prompt_hashtags_only,
            prompt_phrase_plus_hashtags,
            prompt_soft_text_only
        ]

        selected_prompt = random.choice(estilos)
        user_message = self.create_message("user", selected_prompt)

        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).strip('"')

        
    def tikTok_title_elite_spa(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a catchy TikTok title for the following service: {theme}. The title should include a strong keyword, be attractive and end with a relevant emoji only at the end of the comment, and be {characters} in length, without hashtags.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    # ============================= LOPEZ & LOPEZ ABOGADOS  ==============================
    
    def copy_lopez_abogados(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE) 
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a professional and concise text about {theme} related to López & López Abogados (no need to mention the company, just for context). The text should highlight key legal services or benefits, convey trust and expertise, and end with two relevant emojis that maintain a formal tone. If possible, focus on a specific topic based on the legal service, ensuring the copy reflects the firm's legal expertise. Additionally, provide 8 relevant and serious hashtags based on the content. The text should not exceed {characters} characters.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        )
        
    def theme_lopez_abogados(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following legal service: {self.service}, generate a formal and relevant theme that accurately reflects the **nature and importance** of the legal service. The theme should evoke trust, seriousness, and professionalism.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")
    
    def document_title_lopez_abogados(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following legal service: {theme}, provide a **single powerful word** that best represents a key **legal benefit or value** of this service. The word must be concise, impactful, and aligned with **professional legal language**.",
        )        
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")
    
    def youtube_video_title_lopez_abogados(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a professional YouTube title for {theme}, including one strong keyword in ALL CAPS and a **relevant legal emoji** at the end (e.g., ⚖️, 📜). The title must convey **legal authority and trust**, not exceed {characters} characters, and avoid casual phrases. Do not add explanations.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def youtube_video_tags_lopez_abogados(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate 10 **professional and relevant** YouTube tags for {theme}, focusing on the **legal benefits and quick, cost-effective solutions** offered by a law firm. Use a mix of general legal terms and specific service-related keywords. Separate tags with commas, and do not include enumerations or hashtags.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def first_comment_lopez_abogados(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        prompt_hashtags_only = f"""
        You are López & López Abogados — a legal firm based in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official López & López Abogados account** — not a viewer.

        ✳️ Style: Hashtags only.
        - Leave two blank lines at the top.
        - Then insert either 👇👇👇 or … on a single line.
        - On the next line, write 3–4 serious, professional hashtags about legal advice, immigration, personal injury, or Chicago law.
        - Do **not** use emojis or text (except 👇👇👇 or …).
        - Avoid overused tags — rotate combinations and keep tone formal.

        ✅ Max {characters} characters.
        ✅ Must reflect a serious, legal tone.
        ✅ Hashtags must feel unique and not automated.
        """

        prompt_statement_plus_hashtags = f"""
        You are López & López Abogados — a legal firm based in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official López & López Abogados account** — not a viewer.

        ✳️ Style: Short statement + hashtags.
        - Write a concise, formal sentence in first person plural (e.g., "We guide families through complex immigration cases.").
        - Add 1–2 legal-related hashtags.
        - Use **only one legal emoji** (e.g., ⚖️ or 📜) — vary it in each version.
        - Maintain a respectful, professional tone.

        ✅ Max {characters} characters.
        ✅ No links. Avoid repetitive phrases.
        """

        prompt_formal_text_only = f"""
        You are López & López Abogados — a legal firm based in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official López & López Abogados account** — not a viewer.

        ✳️ Style: Formal text only.
        - Use first person plural voice.
        - Craft a respectful, professional sentence that communicates trust, clarity, or commitment.
        - Do **not** include hashtags or links.
        - Optionally include **one legal emoji** to complement the tone (e.g., ⚖️ or 📜).

        ✅ Max {characters} characters.
        ✅ Must feel human, informed, and aligned with a serious law practice.
        """

        estilos = [
            prompt_hashtags_only,
            prompt_statement_plus_hashtags,
            prompt_formal_text_only
        ]

        selected_prompt = random.choice(estilos)
        user_message = self.create_message("user", selected_prompt)

        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).strip('"')

    def tikTok_title_lopez_abogados(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a concise and **professionally worded TikTok title** for the following legal service: {theme}. Include a strong **legal keyword**, maintain a **serious and trustworthy tone**, and end with one **formal emoji** (e.g., ⚖️). Max {characters} characters. Do not include hashtags.",
        )
        return self.generate_response(
            "gpt-4", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    # ============================= BOTÁNICAS MÉTODOS ==============================

    def theme_botanica(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Genera un tema místico para el servicio: '{self.service}'. El tema debe mencionar directamente este, o estar claramente relacionado con él. Usa máximo 8 palabras. No incluyas explicaciones, solo responde el tema.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")


    def copy_botanica(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Escribe un copy impactante sobre {theme}. Incluye un gancho inicial llamativo, la empresa trata sobre amarres, santería, lecturas de tarot, brujería, etc., la idea es que identifiques que tipo de contenido se debe realizar con el tema. Agrega 2 emojis relacionados al tema (al final del texto). No escribas títulos, solo el texto, máximo {characters} caracteres. Además, incluya ocho hashtags relevantes según el contenido.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")
    

    def comment_from_title(self, video_title, campaign_name=None, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        company_name = campaign_name or self.campaign

        user_message = self.create_message(
            "user",
            f"""
            You are writing a **first comment** for a video titled: "{video_title}".

            This comment is posted by the official account of **{company_name}**, not a viewer or external person.

            🎯 Objective:
            Write a short and engaging comment as if it were made by the business itself — a brand voice.
            It should sound like a direct message to the audience, with a friendly and clear tone.

            ✅ Use one of the following formats:
            1️⃣ Just hashtags  
            2️⃣ A short phrase + website link  
            3️⃣ A short question to spark engagement  
            4️⃣ A simple call to action (e.g., "Message us 'QUICK' for a quote!")

            📝 Instructions:
            - Write in **first person plural**: “we”, “our team”, “contact us”, etc.
            - Be friendly, short, and natural (not robotic).
            - **Do not repeat the title**.
            - Max {characters} characters.
            - At most **one emoji**, only if it fits naturally.
            - Keep it suitable for platforms like Facebook, TikTok, or YouTube Shorts.
            """
        )

        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).strip('"')


    def document_title_botanica(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"De acuerdo al tema: {theme}, proporciona solo una palabra clave esotérica que represente un beneficio profundo. No agregues nada más.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")


    def youtube_video_title_botanica(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        banned_words = ["descubre", "descubriendo", "secretos", "secreto", "ocultos", "revelados", "misterios"]
        
        prompt = f"""
        Crea un título original para un video corto de YouTube sobre **{theme}**.

        ✅ Instrucciones:
        – Usa lenguaje **místico, evocador o informativo**, sin sonar comercial.
        – Evita completamente las siguientes palabras: {', '.join(banned_words)}.
        – Usa **una sola palabra en mayúscula**, y colócala naturalmente.
        – Agrega **1 emoji relacionado al tema** (ritual, energía, intuición, limpieza, etc.) al final.
        – No uses palabras como "descubre", "secretos", "misterios", "revelados".
        – No excedas {characters} caracteres.
        – Genera solo el título, sin comillas ni explicación ni descripción.

        Ahora genera el título.
        """

        user_message = self.create_message("user", prompt)
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "").strip()



    def youtube_video_tags_botanica(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Genera 10 tags para YouTube sobre {theme}, relacionados a espiritualidad, amarres, rituales, poder interior, lecturas de tarot, hechizos. Sin hashtags ni números, separados por coma.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")


    def first_comment_botanica(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        prompt_hashtags_only = f"""
        Eres una botánica espiritual con conexión mística con los planos energéticos.

        Escribe el **primer comentario** en tu propio video sobre el tema: "{theme}".
        Este comentario lo publica la **cuenta oficial de la botánica**, no un cliente.

        ✳️ Estilo: Solo hashtags.
        – Deja **dos saltos de línea arriba**.  
        – Luego escribe una línea que contenga solo 👇👇👇 o …  
        – En la siguiente línea, escribe **3 a 4 hashtags esotéricos** relacionados con energía, tarot, amarres, protección, limpieza espiritual.  
        – No uses texto adicional ni emojis (solo 👇👇👇 o …).  
        – Evita combinaciones genéricas como #BuenaVibra o #LimpiezaTotal. Hazlo único y poderoso.

        ✅ Máximo {characters} caracteres.
        ✅ Los hashtags deben sonar auténticos, místicos y no repetitivos.
        """

        prompt_phrase_plus_hashtags = f"""
        Eres una botánica espiritual con sabiduría ancestral.

        Escribe el **primer comentario** en tu propio video sobre el tema: "{theme}".  
        Este comentario lo publica la **cuenta oficial de la botánica**, no un espectador.

        ✳️ Estilo: Frase mística + hashtags.
        – Comienza con una frase energética en primera persona plural (ej: “Conectamos con tu destino” o “Invocamos protección y claridad”).  
        – Añade 1–2 hashtags esotéricos al final.  
        – Puedes usar **un solo emoji místico** si ayuda a reforzar la energía del mensaje (🧿, 🔮, 🌙, etc.).

        ✅ Máximo {characters} caracteres.
        ✅ Nada de enlaces. Los hashtags deben rotar y sentirse auténticos.
        """

        prompt_mystical_text_only = f"""
        Eres una botánica con conocimiento espiritual profundo.

        Escribe el **primer comentario** en tu propio video sobre el tema: "{theme}".  
        Este comentario lo publica la **cuenta oficial de la botánica**, no una persona externa.

        ✳️ Estilo: Solo texto místico.
        – Usa primera persona plural.  
        – Transmite un mensaje lleno de intención, energía o guía espiritual.  
        – No uses hashtags ni links de paginas.  
        – Puedes cerrar con **un emoji místico o neutral** si se siente apropiado (🌿, ✨, 🔮, 🕯️).

        ✅ Máximo {characters} caracteres.
        ✅ El tono debe ser reflexivo, profundo y alineado con lo espiritual.
        """

        estilos = [
            prompt_hashtags_only,
            prompt_phrase_plus_hashtags,
            prompt_mystical_text_only
        ]

        selected_prompt = random.choice(estilos)
        user_message = self.create_message("user", selected_prompt)

        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).strip('"')


    def tikTok_title_botanica(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Crea un título corto para TikTok sobre {theme}. Incluye una palabra fuerte y 1 emoji místico al final. No incluyas hashtags. Máximo {characters} caracteres.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")


    # ============================= SPA312 METHODS ==============================

    def copy_spa312(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate elegant and soothing promotional copy for the theme: {theme}. "
            f"The copy should start with a calming hook, highlight the wellness or beauty benefits of the service, and close with a gentle call to action. "
            f"Add exactly two soft or relaxing emojis at the end. Then, generate 10 fresh and aesthetic hashtags based on the content. "
            f"Limit the copy to {characters} characters max.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")

    def theme_spa312(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following spa service: {self.service}, generate a soft and attractive theme that reflects beauty, self-care, and wellness. It should be poetic but clear.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")

    def document_title_spa312(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Based on the theme: {theme}, suggest one elegant and meaningful word that represents the emotional benefit or aesthetic essence of the spa service.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")

    def youtube_video_title_spa312(self, theme, characters=40):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Create a YouTube video title for the theme: {theme}. It must include a calming or elegant word in all caps, end with one emoji, and stay within {characters} characters.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")

    def youtube_video_tags_spa312(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate 10 relevant YouTube tags for a spa service related to {theme}. Tags should focus on beauty, skincare, relaxation, Chicago spa, and aesthetic services. Separate with commas.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")

    def first_comment_spa312(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        prompt_hashtags_only = f"""
        You are Spa312 — a luxury spa in Chicago offering skincare and wellness.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Spa312 account** — not a viewer.

        ✳️ Style: Hashtags only.
        - Leave two blank lines at the top.
        - Then insert either 👇👇👇 or … on a single line.
        - On the next line, write 3–4 elegant and fresh hashtags related to skincare, spa beauty, glow, self-love, or inner peace.
        - Do **not** include emojis or any other text.
        - Avoid generic hashtags like #RelaxationTime — make them feel curated and premium.

        ✅ Max {characters} characters.
        ✅ Make hashtags feel new, clean, and relaxing.
        """

        prompt_statement_plus_hashtags = f"""
        You are Spa312 — a luxury spa in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Spa312 account** — not a viewer.

        ✳️ Style: Gentle phrase + hashtags.
        - Start with a calming or empowering phrase in first person plural (e.g., "We bring beauty to the surface." or "Our hands restore your glow.").
        - Add 1–2 beauty or spa-related hashtags.
        - One soft emoji allowed (🌸, ✨, 🧖‍♀️, etc.).

        ✅ Max {characters} characters.
        ✅ Avoid hashtags like #SkincareRoutine — use refined variations.
        """

        prompt_text_only = f"""
        You are Spa312 — a luxury spa in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Spa312 account** — not a viewer.

        ✳️ Style: Gentle text only.
        - Use one short sentence in first person plural.
        - The message should feel elegant, healing, or luxurious.
        - No hashtags. One soft emoji allowed at the end if it fits.

        ✅ Max {characters} characters.
        ✅ Must sound calm, premium, and brand-authentic.
        """

        estilos = [
            prompt_hashtags_only,
            prompt_statement_plus_hashtags,
            prompt_text_only
        ]

        selected_prompt = random.choice(estilos)
        user_message = self.create_message("user", selected_prompt)

        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).strip('"')

    def tikTok_title_spa312(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Write a TikTok video title for the spa service: {theme}. The title should feel calming or beautiful, include a powerful keyword, and end with one gentle emoji. Do not include hashtags. Max {characters} characters.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")


    # ============================= ELITE FRENCHIES METHODS ==============================

    def copy_elite_frenchies(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Write an emotional and captivating promotional copy about: {theme}. "
            f"Include a warm hook, highlight the uniqueness and care of Elite Frenchies' puppies, and close with a soft call to action. "
            f"End with two playful or dog-related emojis. Then provide 10 engaging and brand-aligned hashtags. "
            f"The copy must be no more than {characters} characters.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")

    def theme_elite_frenchies(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the service: {self.service}, suggest a heartfelt and catchy theme that reflects Elite Frenchies' quality, care, and love for French Bulldogs.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")

    def document_title_elite_frenchies(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Suggest a single emotional and elegant word that summarizes the core value of the theme: {theme}, related to French Bulldog breeding.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")

    def youtube_video_title_elite_frenchies(self, theme, characters=40):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Create a YouTube title about {theme} for Elite Frenchies. It should include a cute or emotional word in ALL CAPS and end with a puppy emoji. Max {characters} characters.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")

    def youtube_video_tags_elite_frenchies(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate 10 YouTube tags related to the topic: {theme}. The tags should cover French Bulldogs, puppies, dog breeders, family pets, and location (Chicago). Use commas.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")

    def first_comment_elite_frenchies(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        prompt_hashtags_only = f"""
        You are Elite Frenchies — a trusted French Bulldog breeder in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Elite Frenchies account** — not a viewer.

        ✳️ Style: Hashtags only.
        - Leave two line breaks at the top.
        - Then insert either 👇👇👇 or … on a single line.
        - On the next line, write 3–4 cute, premium-looking hashtags related to Frenchies, puppies, or responsible dog breeding.
        - No emojis or regular text (except 👇👇👇 or …).

        ✅ Max {characters} characters.
        ✅ Must feel warm, original, and brand-aligned.
        """

        prompt_statement_plus_hashtags = f"""
        You are Elite Frenchies — a French Bulldog breeder in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Elite Frenchies account** — not a viewer.

        ✳️ Style: Short statement + hashtags.
        - Use first person plural.
        - Keep the tone warm, trustworthy, and dog-loving.
        - Include 1–2 dog-related hashtags.
        - One puppy emoji allowed at the end.

        ✅ Max {characters} characters.
        ✅ No links or repeated phrasing.
        """

        prompt_text_only = f"""
        You are Elite Frenchies — a top breeder of French Bulldogs in Chicago.

        Write the **first comment** on your own video about the topic: "{theme}".
        This comment is posted by the **official Elite Frenchies account** — not a viewer.

        ✳️ Style: Text only.
        - Use a heartfelt or confident sentence in first person plural.
        - No hashtags or links.
        - One dog emoji allowed at the end if it adds value.

        ✅ Max {characters} characters.
        ✅ Must sound natural, caring, and trustworthy.
        """

        estilos = [
            prompt_hashtags_only,
            prompt_statement_plus_hashtags,
            prompt_text_only
        ]

        selected_prompt = random.choice(estilos)
        user_message = self.create_message("user", selected_prompt)

        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).strip('"')

    def tikTok_title_elite_frenchies(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Write a TikTok video title about {theme} for Elite Frenchies. It should include a cute or exciting keyword, feel emotional or playful, and end with a single dog emoji. No hashtags. Max {characters} characters.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")

   
   