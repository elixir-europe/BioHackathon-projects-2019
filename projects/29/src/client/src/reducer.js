const SET_RESULTS = 'SET_RESULTS';
const DELETE_SEARCH = 'DELETE_SEARCH'
const SET_QUERY = 'SET_QUERY';

function reducer(state, action) {
    switch (action.type) {
        case SET_RESULTS: {
            return {
                ...state,
                results: action.data
            }
        }
        case DELETE_SEARCH: {
            return {
                ...state,
                results: [],
                query: ''
            }
        }
        case SET_QUERY: {
            return {
                ...state,
                query: action.data
            }
        }
        default:
            return state
    }
}

export default reducer;
