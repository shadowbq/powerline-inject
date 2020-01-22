from powerline.theme import requires_segment_info
from pathlib import Path


_BEGINNING_OF_LIST = 0
_INJ_SYMBOL = u'\U0001F489 '
highlight_group_default = 'powerline_inject'

@requires_segment_info
def context(pl, segment_info, before=_INJ_SYMBOL, show_env=True, env_list=(), env_highlighter=highlight_group_default):
    '''
    Return the current items of ENV as separate segments. Uses the 'powerline_inject' 
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
        Path('/var/tmp/RI_NOT_YES').touch()
        return []

    segments_list = []
    env_has_value = False

    for item in env_list: 
        highlight_group = env_highlighter
        content = segment_info['environ'].get(item)
        if content:
            env_has_value = True
            if show_env:
                segments_list.append( {'contents': content + " ",'highlight_groups': [highlight_group] })
    
    if show_env:
        first_highlight_group = segments_list[0]['highlight_groups']
    else:
        first_highlight_group = env_highlighter

    # Add the inject symbol UNICODE :syringe: before the first segment
    if env_has_value:
        segments_list.insert(_BEGINNING_OF_LIST, { 'contents': before, 'highlight_groups': [first_highlight_group] })

    return segments_list
