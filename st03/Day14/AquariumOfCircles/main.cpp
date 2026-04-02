#include <SFML/Graphics.hpp>
#include <optional>

#include <random>
#include <vector>

using namespace sf;

const int WINDOW_WIDTH = 1280;
const int WINDOW_HEIGHT = 720;

RenderWindow window;

// Gives you a random number
// between some min and max values (including min and max)
int randomInt(int min, int max)
{
    static std::random_device rd;
    static std::mt19937 rng(rd());
    std::uniform_int_distribution<int> dist(min, max);

    return dist(rng);
}

// Gives you a random color
sf::Color randomColor()
{
    return sf::Color(
        randomInt(0, 255),
        randomInt(0, 255),
        randomInt(0, 255)
    );
}

// Draws a circle
void drawCircle(int x, int y, int radius, Color color)
{
    CircleShape circle = CircleShape(float(radius));
    circle.setFillColor(color);

    // SFML positions shapes by their top-left corner.
    // This centers the circle on (x, y)
    circle.setPosition({ float(x) - float(radius), float(y) - float(radius) });

    window.draw(circle);
}




int n = 100;
std::vector<int> xs;
std::vector<int> ys;
std::vector<int> rs;
std::vector<Color> cs;
std::vector<int> vxs;
std::vector<int> vys;



void initialize()
{
    for (int i = 0; i < n; i++)
    {
        xs.push_back(randomInt(10, WINDOW_WIDTH - 10));
        ys.push_back(randomInt(10, WINDOW_HEIGHT - 10));
        rs.push_back(randomInt(4, 12));
        cs.push_back(randomColor());
        
        int vx = randomInt(-4, 4);
        if (vx == 0)
        {
            vx = 1;
        }
        int vy = randomInt(-4, 4);
        if (vy == 0)
        {
            vy = 1;
        }
        vxs.push_back(vx);
        vys.push_back(vy);
    }
}

void render()
{
    for (int i = 0; i < n; i++)
    {
        drawCircle(xs[i], ys[i], rs[i], cs[i]);

        int newx = xs[i] + vxs[i];
        int newy = ys[i] + vys[i];

        if (newx + rs[i] >= WINDOW_WIDTH || newx - rs[i] <= 0)
        {
            vxs[i] *= -1;
        }
        if (newy + rs[i] >= WINDOW_HEIGHT || newy - rs[i] <= 0)
        {
            vys[i] *= -1;
        }

        xs[i] += vxs[i];
        ys[i] += vys[i];
    }
}






int main()
{
    ContextSettings contextSettings;
    contextSettings.antiAliasingLevel = 8;

    window = RenderWindow(VideoMode({ WINDOW_WIDTH, WINDOW_HEIGHT }), "Aquarium Of Circles", Style::Default, State::Windowed, contextSettings);
    window.setFramerateLimit(60);

    initialize();

    while (window.isOpen())
    {
        while (const std::optional event = window.pollEvent())
        {
            if (event->is<Event::Closed>())
                window.close();
        }

        window.clear(Color::Black);

        render();

        window.display();
    }

    return 0;
}