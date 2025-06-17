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

    def firts_comment_osceola(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        estilos = [
            # Solo hashtags (profesionales)
            f"""
            Write a first comment for "{theme}" using only professional hashtags relevant to fencing, security, and Chicago. 
            Use 2 line breaks above. No text or emojis. Max {characters} characters.
            Use **no more than 4 relevant hashtags** related to cleaning.
            """,

            # Texto + hashtags
            f"""
            You are Osceola Fence. Write a first comment for a video about "{theme}" in first person plural (we/our team). 
            Use a serious but friendly tone. Include a short statement + 2 professional hashtags. One emoji allowed.
            Max {characters} characters.
            """,

            # Solo texto (sin hashtags)
            f"""
            Write a first comment from Osceola Fence about "{theme}" in first person plural. 
            The message should express confidence and professionalism. Avoid hashtags.  
            Use a clean sentence with 1 emoji if appropriate. Max {characters} characters.
            """
        ]

        prompt = random.choice(estilos)
        user_message = self.create_message("user", prompt)

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
        
    def firts_comment_elite_spa(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        estilos = [
            # Solo hashtags
            f"""
            You are Elite Chicago Spa. Write a first comment for a video about "{theme}" using only soft, elegant hashtags about self-care, beauty, and wellness.  
            Leave 2 line breaks above. No emojis. Max {characters} characters.
            Use **no more than 4 relevant hashtags** related to cleaning.
            """,

            # Texto + hashtags
            f"""
            Write a first comment from Elite Chicago Spa for the topic "{theme}". 
            Use a warm tone in first person plural. Write a gentle phrase and include 1–2 spa-related hashtags. Optional: 1 emoji. Max {characters} characters.
            """,

            # Solo texto
            f"""
            Write a first comment as Elite Chicago Spa about "{theme}" using first person plural.  
            Focus on comfort, beauty, and care. Avoid hashtags. Include a soft emoji if needed. Max {characters} characters.
            """
        ]

        prompt = random.choice(estilos)
        user_message = self.create_message("user", prompt)

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

    def firts_comment_lopez_abogados(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        estilos = [
            # Solo hashtags (legales)
            f"""
            Write a first comment for "{theme}" using only serious, professional hashtags related to legal services in Chicago.  
            Leave 2 blank lines above. No emojis or extra text. Max {characters} characters.
            Use **no more than 4 relevant hashtags** related to cleaning.
            """,

            # Texto + hashtags
            f"""
            You are López & López Abogados. Write a professional first comment about "{theme}" in first person plural.  
            Use a short statement + 1–2 legal hashtags. One ⚖️ or 📜 emoji allowed. Max {characters} characters.
            """,

            # Solo texto
            f"""
            Write a serious and professional first comment from López & López Abogados for "{theme}".  
            Keep a respectful and formal tone. Use first person plural. No hashtags. One legal emoji max. Max {characters} characters.
            """
        ]

        prompt = random.choice(estilos)
        user_message = self.create_message("user", prompt)

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
        user_message = self.create_message(
            "user",
            f"Crea un título de YouTube llamativo sobre {theme}, incluye una palabra en mayúscula y 1 emoji relacionado con el titulo al final. Máximo {characters} caracteres. Solo el título, sin descripción.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")


    def youtube_video_tags_botanica(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Genera 10 tags para YouTube sobre {theme}, relacionados a espiritualidad, amarres, rituales, poder interior, lecturas de tarot, hechizos. Sin hashtags ni números, separados por coma.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")


    def firts_comment_botanica(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)

        estilos = [
            # Solo hashtags (espirituales)
            f"""
            Escribe un primer comentario desde la perspectiva de una botánica mística para el tema "{theme}".  
            Solo incluye hashtags relacionados con espiritualidad, amarres, energía, tarot, limpieza.  
            Deja dos saltos de línea arriba. No agregues texto ni emojis. Máximo {characters} caracteres.
            Utiliza **no más de 4 hashtags relevantes** relacionados con la limpieza.
            """,

            # Texto + hashtags
            f"""
            Eres una botánica espiritual. Escribe un comentario para el video sobre "{theme}" en primera persona plural.  
            Incluye una frase con energía mística + 1–2 hashtags esotéricos. Máximo 1 emoji. Máximo {characters} caracteres.
            """,

            # Solo texto
            f"""
            Escribe un primer comentario para "{theme}" desde la cuenta oficial de una botánica.  
            Usa primera persona plural. Hazlo reflexivo, energético, sin hashtags. Puedes cerrar con un emoji si aplica. Máximo {characters} caracteres.
            """
        ]

        prompt = random.choice(estilos)
        user_message = self.create_message("user", prompt)

        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).strip('"')


    def tikTok_title_botanica(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Crea un título corto para TikTok sobre {theme}. Incluye una palabra fuerte y 1 emoji místico al final. No incluyas hashtags. Máximo {characters} caracteres.",
        )
        return self.generate_response("gpt-4", [system_message, assistant_message, user_message]).replace('"', "")

        

    
   
   