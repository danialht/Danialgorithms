#include <vector>
#include <algorithm>

using std::vector;

class Kosaraju{
    private:
    int* out_time;
    bool* visited;
    vector<int> scc;
    int t = 0;
    vector<vector<int>> g;

    void dfs(int x, vector<vector<int>>& g, vector<int>& vec){
        visited[x] = true;
        for(auto u : g[x]){
            if(visited[u]) continue;
            dfs(u, g, vec);
        }
        out_time[x] = t;
        vec.push_back(x);
        t++;
    }

    public:
    Kosaraju(vector<vector<int>>& g){
        this->g = g;
        this->visited = new bool[g.size()];
        this->out_time = new int[g.size()];
    }

    vector<int> run(){
        int n = g.size();
        vector<int> order;
        for(int i = 0 ; i < n ; i++) visited[i] = false;
        for(int i = 0 ; i < n ; i++){
            if(!visited[i])
                dfs(i, g, order);
        }

        std::reverse(order.begin(), order.end());
        
        vector<vector<int>> grev;
        for(int i = 0 ; i < n ; i++) grev.push_back({});
        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j < g[i].size() ; j++)
                grev[g[i][j]].push_back(i);
        }

        vector<vector<int>> sccs;
        
        for(int i = 0 ; i < n ; i++){scc.push_back(0);visited[i] = false;}
        for(int i = 0 ; i < n ; i++){
            if(visited[order[i]]) continue;
            sccs.push_back({});
            dfs(order[i], grev, sccs[sccs.size() - 1]);
        }

        for(int i = 0 ; i < sccs.size() ; i++)
            for(int j = 0 ; j < sccs[i].size() ; j++)
                scc[sccs[i][j]] = i;


        return scc;
    }

};