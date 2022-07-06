from django.shortcuts import render, get_object_or_404
from .models import Hangman
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HangmanGameView(APIView):
    def get_game_data(self, game):
        return {
            'word': ''.join(list(map(lambda c: c if c in game.tried_chars else "_", game.word))),
            'tried_chars': ''.join(list(map(lambda c: c if c not in game.word else "", game.tried_chars))),
            'try_count': len(game.tried_chars),
            'max_try': game.max_try
        }

    def get(self, request, *args, **kwargs):
        game = get_object_or_404(Hangman, id=kwargs['id'])
        print(game)
        return Response(self.get_game_data(game))

    def post(self, request, *args, **kwargs):
        game = get_object_or_404(Hangman, id=kwargs['id'])
        if len(game.tried_chars) >= game.max_try:
            return Response({"error": "you have tried the maximum amount"})
        if not request.data.get('char') or len(request.data.get('char')) != 1 or not request.data.get('char').isalpha():
            return Response({"error": "the request is undefined or malformed"}, status=400)
        elif request.data.get('char') in game.tried_chars:
            pass
        else:
            game.tried_chars = ''.join(
                sorted(game.tried_chars + request.data.get('char')))
            game.save()
        return Response(self.get_game_data(game))


class CreateGameView(APIView):
    def post(self, request, *args, **kwargs):
        if not request.data.get('word'):
            return Response({"error": "word is required"})
        if request.data.get('max_try'):
            max_try = request.data.get('max_try')
        else:
            max_try = 7
        game = Hangman.objects.create(word=''.join(list(map(lambda c: c if c.isalpha(
        ) else "", request.data.get('word')))).lower(), max_try=max_try)
        return Response({"id": game.id, "word": game.word, "max_try": game.max_try})
