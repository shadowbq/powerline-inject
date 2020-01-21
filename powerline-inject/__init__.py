from powerline.theme import requires_segment_info

_INJ_SYMBOL = u'\U0001F489 '
#:syringe:

@requires_segment_info
def context(pl, segment_info, show_env=True, env_list=()):
    '''
    Return the current items of envs as separate segments. Uses the 'kubernetes_cluster' 
    highlight groups.

    Because you may not want your inject context in your status bar at all times, you can
    disable it by setting an environment variable 'RENDER_POWERLINE_INJECTS' to anything
    other than true. One way to do this would be with a simple function, such as putting this
    in your ~/.bash_profile:

        pl-injects() {
            if [[ $RENDER_POWERLINE_INJECTS = "NO" ]]; then
                export RENDER_POWERLINE_INJECTS=YES
            else
                export RENDER_POWERLINE_INJECTS=NO
            fi
        }

    Then you can toggle showing your injects in powerline by just typing `pl-injects`
    in your terminal
    '''
    pl.debug('Running powerline-inject')

    render_injects = segment_info['environ'].get('RENDER_POWERLINE_INJECTS', 'YES')
    if render_injects != 'YES':
        return []

    if not any([show_env]):
        return []

    segments_list = []

    if show_env:
        for item in env_list: 
            highlight_group = 'powerline_inject'
            segments_list.append(
            {'contents': item,
             'highlight_groups': [highlight_group],
             }
        )


    # Add the inject symbol before the first segment
    first_highlight_group = segments_list[0]['highlight_groups']
    segments_list.insert(0, {'contents': _INJ_SYMBOL,
                             'highlight_groups': first_highlight_group
                             }
                         )
    return segments_list
