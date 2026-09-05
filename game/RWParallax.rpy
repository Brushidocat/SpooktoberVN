# Parallax Shader for Ren’Py
# Free to use with credit.
# Credit: Rythen Winds — https://rythen-winds.itch.io/

transform parallax_shift(z_pos = 0.5,sprite = True, strength=0.02):
    mesh True
    gl_drawable_resolution True
    shader 'depth_parallax.shader'
    u_index_z (z_pos)
    u_is_sprite (1.0 if sprite else 0.0)
    u_parallax_strength (strength)
    function set_mouse_pos

init python:
    def inv_lerp(a, b, v) -> float:
        """Inverse Linear Interpolation, get the fraction between a and b on which v resides.
        Examples
        --------
            0.5 == inv_lerp(0, 100, 50)
            0.8 == inv_lerp(1, 5, 4.2)
        """
        return (v - a) / (b - a)
    
    def set_mouse_pos(trans, st, at):
        x, y = renpy.display.draw.get_mouse_pos()
        trans.u_mouse_x = inv_lerp(0, config.screen_width, (x - config.screen_width / 2))
        trans.u_mouse_y = inv_lerp(0, config.screen_height, (y - config.screen_height / 2))
        return 0

init -2 python:
    renpy.register_shader("depth_parallax.shader", variables="""
        varying vec2 v_tex_coord;
        varying vec2 v_position;

        uniform float u_mouse_x;
        uniform float u_mouse_y;
        uniform float u_index_z;

        uniform float u_is_sprite;
        uniform float u_parallax_strength;

        attribute vec4 a_position;
        attribute vec2 a_tex_coord;

    """, fragment_functions="""

    """, vertex_300="""
        v_tex_coord = a_tex_coord;
        v_position = a_position.xy;
    """, fragment_350="""

        vec2 mouse = vec2(u_mouse_x, u_mouse_y); // Gets the mouse pos for effect.

        // Set up parallax: for sprites, scale up the movement to compensate for size
        vec2 parallax = mouse * u_index_z * u_parallax_strength;

        bool is_sprite = (u_is_sprite > 0.5);
        if (is_sprite){
            parallax.x *= 10.0;  // Increase horizontal parallax for sprites
            parallax.y *= 1.0;    // subtle vertical parallax, you can change this. 0 for no vertical.
        }

        // Set anchor for zoom: bottom center for sprites
        vec2 pivot = is_sprite ? vec2(0.5, 1.0) : vec2(0.5, 0.5);

        // Applying parallax
        vec2 uv = (v_tex_coord - pivot) / 1.0 + pivot + parallax;

        // Clamp not actually needed in this case.
        // uv = clamp(uv, 0.0, 1.0);

        gl_FragColor = texture2D(tex0, uv);
    """
    )