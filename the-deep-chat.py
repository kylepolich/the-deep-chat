import actions_pb2 as objs


def get_tdc_rss_pipeline():
    params1 = objs.Parameter(var_name='stream_id', ptype=objs.ParameterType.FEED_ID)
    output1 = objs.Parameter(var_name='rss_dest_key', ptype=objs.ParameterType.KEY)
    static_values = {
        "dest_ext": objs.AnyType(ptype=objs.ParameterType.PARAMETER_MAP, sval=?),
        "var_map"
    }
    action_id1 = 'feaas-py.chalicelib.actions.convert.stream2podcast.Stream2Podcast'
    map1i1 = objs.ParameterMap(src='stream_id', dest='stream_id')
    map1i2 = objs.ParameterMap(src='var_map', dest='varmap')
    map1i3 = objs.ParameterMap(src='dest_key', dest='dest_key')
    stream_id, varmap, dest_key


def get_tdc_production_pipeline():
    v1 = objs.Validation(vtype=objs.ValidationType.EXISTS)
    v2 = objs.Validation(vtype=objs.ValidationType.ENDS_WITH, sval='.wav')
    params1 = objs.Parameter(
        var_name='src_key',
        label='Source file',
        ptype=objs.ParameterType.KEY,
        validations=[v1, v2])
    output1 = objs.Parameter(var_name='mp4_dest_key', ptype=objs.ParameterType.KEY)
    static_values = {
        # "dest_ext": objs.AnyType(ptype=objs.ParameterType.STRING, sval='.html'),
        # "pub_prefix": objs.AnyType(ptype=objs.ParameterType.PREFIX, sval="user/kyle@dataskeptic.com/dataskeptic/pub/blog/"),
        # "stream_id": objs.AnyType(ptype=objs.ParameterType.FEED_ID, sval="kyle@dataskeptic.com/stream.com.dataskeptic.blog")
    }
    action_id1 = 'feaas-py.chalicelib.actions.vendor.aws.transcribe.transcribe.Transcribe'
    # TODO: output html doc
    # TODO: publish transcript to site
    # TODO: transform transcript to timeline
    # TODO: ffmpeg with faces
    # action_id2 = 'feaas-py.chalicelib.actions.convert.markdown2html.Markdown2Html'
    # action_id3 = 'feaas-py.chalicelib.actions.load.text2file.Text2File'
    # action_id4 = 'feaas-py.chalicelib.actions.load.name_sibling.NameSibling'
    # action_id5 = 'feaas-py.chalicelib.actions.sys.move.MoveFile'
    # action_id6 = 'feaas-py.chalicelib.actions.stream.add.AddToStream'
    #
    map1i1 = objs.ParameterMap(src='username', dest='username')
    map1i2 = objs.ParameterMap(src='src_key', dest='src_key')
    map1i2 = objs.ParameterMap(src='mp3_ext', dest='dest_ext')
    map1o1 = objs.ParameterMap(src='job_id', dest='transcribe_job_id')
    #
    step1 = objs.PortalScriptStep(
        step_id='s1',
        action_id=action_id1,
        in_map=[map1i1, map1i2, map1i3],
        out_map=[map1o1],
        label='Transcribe')
    steps = [ step1 ]
    desc = ''
    return objs.PortalScript(
        object_id='kyle@dataskeptic.com/pscript.the_deep_chat_production_pipeline',
        owner='kyle@dataskeptic.com/pscript',
        version='v0.0.1',
        label='The Deep Chat publishing',
        short_desc=desc,
        long_desc=desc,
        fa_icon='fa-code',
        params=[params1],
        static_values=static_values,
        steps=steps,
        outputs=[output1])


def get_podcast_release_pipeline():
    desc = 'Run to update our site when the RSS feed is updated.'
    output1 = objs.Parameter(var_name='blog_page', ptype=objs.ParameterType.URL)
    static_values = {
        "rss_url": objs.AnyType(ptype=objs.ParameterType.URL, sval='http://dataskeptic.libsyn.com/rss'),
        "dest_stream_id": objs.AnyType(ptype=objs.ParameterType.FEED_ID, sval='kyle@dataskeptic.com/stream.com.dataskeptic.podcast'),
        "copy": objs.AnyType(ptype=objs.ParameterType.BOOLEAN, bval=True),
        "dest_prefix": objs.AnyType(ptype=objs.ParameterType.PREFIX, sval='user/kyle@dataskeptic.com/dataskeptic/pub/mp3/')
    }
    #
    update_feed_in = [
        objs.ParameterMap(src='username', dest='username'),
        objs.ParameterMap(src='rss_url', dest='rss_url'),
        objs.ParameterMap(src='dest_stream_id', dest='dest_stream_id'),
        objs.ParameterMap(src='copy', dest='copy_media'),
        objs.ParameterMap(src='dest_prefix', dest='dest_prefix')
    ]
    action_id1 = 'feaas-py.chalicelib.actions.stream.poll.rss2stream.Rss2Stream'
    #
    params = []
    outputs = [output1]
    steps = []
    steps.append(objs.PortalScriptStep(step_id='s1', label='update_feed', action_id=action_id1, in_map=update_feed_in, out_map=[]))
    # TODO: how to make s2 depend on s1
    # steps.append(objs.PortalScriptStep(step_id='s2', label='merge_to_blog_feed', action_id=?, in_map=[?], out_map=[?]))
    # steps.append(objs.PortalScriptStep(step_id='s3', label='download_audio', action_id=?, in_map=[mp3_key, num_speakers], out_map=[transcription_out_key]))
    # steps.append(objs.PortalScriptStep(step_id='s3', label='transcribe', action_id=?, in_map=[mp3_key, num_speakers], out_map=[transcription_out_key]))
    # steps.append(objs.PortalScriptStep(step_id='s4', label='link_player_to_blog', action_id=?, in_map=[mp3_key, num_speakers], out_map=[transcription_out_key]))
    # steps.append(objs.PortalScriptStep(step_id='s4', label='link_guest_to_blog', action_id=?, in_map=[mp3_key, num_speakers], out_map=[transcription_out_key]))
    # steps.append(objs.PortalScriptStep(step_id='s5', label='update_homepage', action_id=?, in_map=[mp3_key, num_speakers], out_map=[transcription_out_key]))
    return objs.PortalScript(
        object_id='kyle@dataskeptic.com/pscript.podcast_release_pipeline',
        owner='kyle@dataskeptic.com/pscript',
        version='v0.0.1',
        label='Post-release pipeline',
        short_desc=desc,
        long_desc=desc,
        fa_icon='fa-rss',
        params=params,
        static_values=static_values,
        steps=steps,
        outputs=outputs)



# brad
# auphonic


# data = {}
# for k in contents.keys():
#     val = contents[k]
#     data[k] = util.any_type_ifier(val)


