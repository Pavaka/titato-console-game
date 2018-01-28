#include <TitatoGame.h>
#include <iostream>
int main()
{
	auto game = pavakalib::TitatoGame::CreateGame();

	std::cout << game->Dummy() << "\n";
	pavakalib::TitatoGame::DestroyGame(game);
	return 0;
}