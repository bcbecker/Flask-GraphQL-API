all_employees_query = '''query{
  allEmployees {
    edges {
      node {
        id,
        name,
        hiredOn,
        department {
          id,
          name
        },
        roles {
          edges {
            node {
              id,
              name
            }
          }
        },
        manager {
          id,
          name
        }
        tasks {
          edges {
            node {
              name,
              deadline
            }
          }
        }
      }
    }
  }
}'''