def generate_postfix(counter):
    """Custom postfix pattern"""
    custom_sequence = 'y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x'
    sequence_list = custom_sequence.split(',')

    sequence_position = counter % len(sequence_list)

    if counter < len(sequence_list):
        return f"00{sequence_list[sequence_position]}""
    elif counter < len(sequence_list) * 26:
        sequence_position = (counter // len(sequence_list)) % len(sequence_list)
        return f"0{sequence_list[sequence_position]}{sequence_list[sequence_list]}"
    else:
        pass


