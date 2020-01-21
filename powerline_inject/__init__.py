from powerline.theme import requires_segment_info

_BEGINNING_OF_LIST=0
_INJ_SYMBOL = u'\U0001F489 '

@requires_segment_info
def context(pl, segment_info, show_env=True, env_list=()):
    '''
    Return the current items of envs as separate segments. Uses the 'powerline_inject' 
    highlight groups.

    By default powerline-inject will render the environment variable if `RENDER_POWERLINE_INJECTS` is 
    either set to `YES` or is not set at all. Rather than setting this variable manually, you can create 
    a simple `powerline-inject-toggle` function by placing the following in your `~/.bash_profile`:


        function powerline-injects-toggle() {
            if [[ $RENDER_POWERLINE_INJECTS = "NO" ]]; then
                export RENDER_POWERLINE_INJECTS="YES"
            else
                export RENDER_POWERLINE_INJECTS="NO"
            fi
        }

    Then you can toggle showing your injects in powerline by just typing `pl-injects`
    in your terminal
    '''
    pl.debug('Running powerline-inject')

    render_injects = segment_info['environ'].get('RENDER_POWERLINE_INJECTS', 'YES')
    if render_injects != 'YES':
        return []

    segments_list = []

    if show_env:
        for item in env_list: 
            highlight_group = 'powerline_inject'
            segments_list.append(
            {'contents': segment_info['environ'].get(item) + " ",
             'highlight_groups': [highlight_group],
             }
        )

    # Add the inject symbol UNICODE :syringe: before the first segment
    first_highlight_group = segments_list[0]['highlight_groups']
    segments_list.insert(   
                            _BEGINNING_OF_LIST, 
                            {
                                'contents': _INJ_SYMBOL,
                                'highlight_groups': first_highlight_group
                            }
                         )
    return segments_list
