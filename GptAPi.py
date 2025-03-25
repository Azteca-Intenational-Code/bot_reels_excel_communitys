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
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def theme_osceola(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {self.service}, provide a theme that captures the essence of the service. The theme should be engaging, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def document_title_osceola(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {theme}, provide a single word that best represents an important characteristic or benefit of this service. The word should be concise, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def youtube_video_title_osceola(self, theme, characters=40):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Give me a YouTube title with a catchy word in all caps and emoji at the end for: {theme} and the title should be {characters} characters long",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def youtube_video_tags_osceola(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a list of relevant YouTube tags for the following service: {theme}. Tags should relate to the service's benefits, features, location in Chicago, and common search terms used by potential customers. Provide a mix of general and specific keywords to maximize visibility, separated by commas, should be ten words.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def firts_comment_osceola(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a short and engaging first comment for a video about {theme}. The comment should sound natural and authentic, as if it came from a real person, without seeming spammy. It's important to note that the comment is made directly by the company, so it should be attention-grabbing to encourage people to comment. It should subtly foster interaction with a question or a friendly remark. Avoid overused phrases and make it feel personal. Use only one emoji at the end if appropriate. The comment should be {characters} characters long.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def tikTok_title_osceola(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a catchy TikTok title for the following service: {theme}. The title should include a strong keyword, be attractive and end with a relevant emoji only at the end of the comment, and be {characters} in length, without hashtags.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
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
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
    
    def theme_quick_cleaning(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {self.service}, provide a theme that captures the essence of the service. The theme should be engaging, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def document_title_quick_cleaning(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {theme}, provide a single word that best represents an important characteristic or benefit of this service. The word should be concise, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def youtube_video_title_quick_cleaning(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Give me a YouTube title with a catchy word in all caps and emoji at the end for: {theme} and the title should be {characters} characters long",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def youtube_video_tags_quick_cleaning(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate 10 short, relevant YouTube tags for {theme}, focusing on its quick and cost-effective benefits. Tags should be a combination of general and specific keywords, each separated by commas. Remember to do not include enumerations and hashtags.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def firts_comment_quick_cleaning(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a short and engaging first comment for a video about {theme}. The comment should sound natural and authentic, as if it came from a real person, without seeming spammy. It's important to note that the comment is made directly by the company, so it should be attention-grabbing to encourage people to comment. It should subtly foster interaction with a question or a friendly remark. Avoid overused phrases and make it feel personal. Use only one emoji at the end if appropriate. The comment should be {characters} characters long.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def tikTok_title_quick_cleaning(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a catchy TikTok title for the following service: {theme}. The title should include a strong keyword, be attractive and end with a relevant emoji only at the end of the comment, and be {characters} in length, without hashtags.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
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
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def theme_elite_spa(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {self.service}, provide a theme that captures the essence of the service. The theme should be engaging, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def document_title_elite_spa(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following service: {theme}, provide a single word that best represents an important characteristic or benefit of this service. The word should be concise, relevant, and impactful.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def youtube_video_title_elite_spa(self, theme, characters=40):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE) 
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a catchy title for a short video about {theme}. The title should be engaging, relevant, and impactful. It should be {characters} characters long.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def youtube_video_tags_elite_spa(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a list of relevant YouTube tags for the following service: {theme}. Tags should relate to the service's benefits, features, location in Chicago, and common search terms used by potential customers. Provide a mix of general and specific keywords to maximize visibility, separated by commas, should be ten words.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def firts_comment_elite_spa(self, theme, characters=90):        
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a short and engaging first comment for a video about {theme}. The comment should sound natural and authentic, as if it came from a real person, without seeming spammy. It's important to note that the comment is made directly by the company, so it should be attention-grabbing to encourage people to comment. It should subtly foster interaction with a question or a friendly remark. Avoid overused phrases and make it feel personal. Use only one emoji at the end if appropriate. The comment should be {characters} characters long.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def tikTok_title_elite_spa(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a catchy TikTok title for the following service: {theme}. The title should include a strong keyword, be attractive and end with a relevant emoji only at the end of the comment, and be {characters} in length, without hashtags.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
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
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        )
        
    def theme_lopez_abogados(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following legal service: {self.service}, generate a formal and relevant theme that accurately reflects the **nature and importance** of the legal service. The theme should evoke trust, seriousness, and professionalism.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
    
    def document_title_lopez_abogados(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Given the following legal service: {theme}, provide a **single powerful word** that best represents a key **legal benefit or value** of this service. The word must be concise, impactful, and aligned with **professional legal language**.",
        )        
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
    
    def youtube_video_title_lopez_abogados(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a professional YouTube title for {theme}, including one strong keyword in ALL CAPS and a **relevant legal emoji** at the end (e.g., ⚖️, 📜). The title must convey **legal authority and trust**, not exceed {characters} characters, and avoid casual phrases. Do not add explanations.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    def youtube_video_tags_lopez_abogados(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate 10 **professional and relevant** YouTube tags for {theme}, focusing on the **legal benefits and quick, cost-effective solutions** offered by a law firm. Use a mix of general legal terms and specific service-related keywords. Separate tags with commas, and do not include enumerations or hashtags.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def firts_comment_lopez_abogados(self, theme, characters=90):
        
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a **formal and trustworthy first comment** for a video about {theme}. The comment must reflect the **voice of a professional law firm**, express respect, and subtly invite interaction through a **thoughtful legal remark or question**. Avoid casual phrases. Conclude with one **appropriate legal emoji**. Max {characters} characters."
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")

    def tikTok_title_lopez_abogados(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Generate a concise and **professionally worded TikTok title** for the following legal service: {theme}. Include a strong **legal keyword**, maintain a **serious and trustworthy tone**, and end with one **formal emoji** (e.g., ⚖️). Max {characters} characters. Do not include hashtags.",
        )
        return self.generate_response(
            "gpt-3.5-turbo", [system_message, assistant_message, user_message]
        ).replace('"', "")
        
    # ============================= BOTÁNICAS MÉTODOS ==============================

    def theme_botanica(self):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Genera un tema místico para el servicio: '{self.service}'. El tema debe mencionar directamente este, o estar claramente relacionado con él. Usa máximo 8 palabras. No incluyas explicaciones, solo responde el tema.",
        )
        return self.generate_response("gpt-3.5-turbo", [system_message, assistant_message, user_message]).replace('"', "")


    def copy_botanica(self, theme, characters=100):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Escribe un copy impactante sobre {theme}. Incluye un gancho inicial llamativo, la empresa trata sobre amarres, santería, lecturas de tarot, brujería, etc., la idea es que identifiques que tipo de contenido se debe realizar con el tema. Agrega 2 emojis relacionados al tema (al final del texto). No escribas títulos, solo el texto, máximo {characters} caracteres. Además, incluya ocho hashtags relevantes según el contenido.",
        )
        return self.generate_response("gpt-3.5-turbo", [system_message, assistant_message, user_message]).replace('"', "")
    

    def document_title_botanica(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"De acuerdo al tema: {theme}, proporciona solo una palabra clave esotérica que represente un beneficio profundo. No agregues nada más.",
        )
        return self.generate_response("gpt-3.5-turbo", [system_message, assistant_message, user_message]).replace('"', "")


    def youtube_video_title_botanica(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Crea un título de YouTube llamativo sobre {theme}, incluye una palabra en mayúscula y 1 emoji relacionado con el titulo al final. Máximo {characters} caracteres. Solo el título, sin descripción.",
        )
        return self.generate_response("gpt-3.5-turbo", [system_message, assistant_message, user_message]).replace('"', "")


    def youtube_video_tags_botanica(self, theme):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Genera 10 tags para YouTube sobre {theme}, relacionados a espiritualidad, amarres, rituales, poder interior, lecturas de tarot, hechizos. Sin hashtags ni números, separados por coma.",
        )
        return self.generate_response("gpt-3.5-turbo", [system_message, assistant_message, user_message]).replace('"', "")


    def firts_comment_botanica(self, theme, characters=90):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Genera un primer comentario para YouTube sobre {theme}. Que suene auténtico, humanizado, místico y genere interacción, es importante que el comentario parezca realizado por la empresa. Incluye máximo 1 emoji. Máximo {characters} caracteres.",
        )
        return self.generate_response("gpt-3.5-turbo", [system_message, assistant_message, user_message]).replace('"', "")


    def tikTok_title_botanica(self, theme, characters=50):
        system_message = self.create_message("system", self.SYSTEM_MESSAGE)
        assistant_message = self.create_message("assistant", self.ASSISTANT_MESSAGE)
        user_message = self.create_message(
            "user",
            f"Crea un título corto para TikTok sobre {theme}. Incluye una palabra fuerte y 1 emoji místico al final. No incluyas hashtags. Máximo {characters} caracteres.",
        )
        return self.generate_response("gpt-3.5-turbo", [system_message, assistant_message, user_message]).replace('"', "")

        

    
   
   