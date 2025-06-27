import sys
import tests.streamlit_stub as st
sys.modules["streamlit"] = st
import template as t


def test_no_duplicate_addition():
    # start with a single friend
    st.session_state.clear()
    st.session_state["Friends"] = [1]

    # attempt to add the same friend again
    friendid = "1"
    if friendid.isdigit() and int(friendid) in st.session_state["Friends"]:
        pass
    elif friendid.isdigit():
        st.session_state["Friends"].append(int(friendid))
        t.add_friend(st.session_state["Friends"])

    assert st.session_state["Friends"] == [1]
