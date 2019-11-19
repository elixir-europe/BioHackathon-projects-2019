
const SET_RESULTS = 'SET_RESULTS';

const DELETE_SEARCH = 'DELETE_SEARCH'

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
        default:
            return state
    }
}

export default reducer;
