import { useState } from 'react'
import { Search, Code2, FileText, Zap, Smartphone } from 'lucide-react'
import toast from 'react-hot-toast'

export default function SEOAnalyzer() {
  const [url, setUrl] = useState('')
  const [analyzing, setAnalyzing] = useState(false)
  const [analyzed, setAnalyzed] = useState(false)

  const handleAnalyze = () => {
    if (!url) {
      toast.error('Please enter a URL')
      return
    }
    
    setAnalyzing(true)
    setTimeout(() => {
      setAnalyzing(false)
      setAnalyzed(true)
      toast.success('Analysis complete!')
    }, 3000)
  }

  const analysisResults = [
    { title: 'Technical SEO', score: 92, issues: 3, icon: Code2, color: 'from-blue-500 to-cyan-500' },
    { title: 'On-Page SEO', score: 85, issues: 7, icon: FileText, color: 'from-purple-500 to-pink-500' },
    { title: 'Performance', score: 88, issues: 5, icon: Zap, color: 'from-green-500 to-emerald-500' },
    { title: 'Mobile Usability', score: 91, issues: 2, icon: Smartphone, color: 'from-orange-500 to-red-500' },
  ]

  return (
    <div className="space-y-6">
      <div className="bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-lg">
        <h2 className="text-2xl font-bold mb-6 text-gray-900 dark:text-white">
          SEO Website Analyzer
        </h2>
        
        <div className="flex space-x-3">
          <input
            type="url"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="https://example.com"
            className="flex-1 px-4 py-3 rounded-xl border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-900 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            onClick={handleAnalyze}
            disabled={analyzing}
            className="px-6 py-3 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-xl font-semibold hover:scale-105 transition-transform flex items-center space-x-2 disabled:opacity-50"
          >
            {analyzing ? (
              <>
                <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
                <span>Analyzing...</span>
              </>
            ) : (
              <>
                <Search className="w-5 h-5" />
                <span>Analyze</span>
              </>
            )}
          </button>
        </div>
      </div>

      {analyzed && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {analysisResults.map((item, index) => {
            const Icon = item.icon
            return (
              <div
                key={index}
                className="bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-lg hover-lift animate-slide-up"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <div className="flex items-center justify-between mb-4">
                  <div className={`w-12 h-12 bg-gradient-to-br ${item.color} rounded-xl flex items-center justify-center`}>
                    <Icon className="w-6 h-6 text-white" />
                  </div>
                  <span className={`text-2xl font-bold ${
                    item.score > 90 ? 'text-green-500' : 
                    item.score > 70 ? 'text-yellow-500' : 
                    'text-red-500'
                  }`}>
                    {item.score}%
                  </span>
                </div>
                <h3 className="text-lg font-semibold mb-2 text-gray-900 dark:text-white">
                  {item.title}
                </h3>
                <p className="text-sm text-gray-600 dark:text-gray-400">
                  {item.issues} issues found
                </p>
                <div className="mt-4">
                  <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
                    <div 
                      className={`h-2 rounded-full bg-gradient-to-r ${item.color}`}
                      style={{ width: `${item.score}%` }}
                    />
                  </div>
                </div>
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}